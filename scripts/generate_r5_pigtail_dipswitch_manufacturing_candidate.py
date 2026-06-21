#!/usr/bin/env python3
import pcbnew
from pathlib import Path

PROJECT = Path('/home/kali/teensy-41-can-lin-pcb')
OUT = PROJECT / 'teensy-41-can-lin-r5-pigtail-dipswitch.kicad_pcb'
FP_ROOT = Path('/usr/share/kicad/footprints')
MM = pcbnew.FromMM


def V(x, y): return pcbnew.VECTOR2I(MM(x), MM(y))

board = pcbnew.BOARD()


def net(name):
    n = board.FindNet(name)
    if n: return n
    ni = pcbnew.NETINFO_ITEM(board, name)
    board.Add(ni)
    return ni

NETS = [
    'GND', '+12V_OBD', '+12V_PROTECTED', '+5V_REGULATED', '+3V3',
    'CAN_A_H', 'CAN_A_L', 'CAN_B_H', 'CAN_B_L',
    'CAN_A_TX', 'CAN_A_RX', 'CAN_B_TX', 'CAN_B_RX', 'CAN_A_STB', 'CAN_B_STB',
    'LIN_BUS', 'LIN_TX', 'LIN_RX', 'LIN_EN',
    'OBD1_SINGLE_WIRE_CANDIDATE', 'OBD2_SPARE_PWM_J1850_CANDIDATE',
    'OBD3_CAN_B_PAIR_A_CANDIDATE', 'OBD6_CAN_A_PAIR_A',
    'OBD7_SINGLE_WIRE_CANDIDATE', 'OBD8_SINGLE_WIRE_CANDIDATE',
    'OBD9_SINGLE_WIRE_CANDIDATE', 'OBD10_SPARE_PWM_J1850_CANDIDATE',
    'OBD11_CAN_B_PAIR_B_CANDIDATE', 'OBD12_SINGLE_WIRE_CANDIDATE',
    'OBD13_SINGLE_WIRE_CANDIDATE', 'OBD14_CAN_A_PAIR_B',
    'OBD15_SINGLE_WIRE_CANDIDATE', 'AUX_LIN_K_IO',
]
for n in NETS: net(n)


def add_fp(path, name, ref, val, x, y, rot=0, padnets=None):
    fp = pcbnew.FootprintLoad(str(path), name)
    if fp is None: raise RuntimeError(f'missing footprint {path}/{name}')
    fp.SetReference(ref); fp.SetValue(val); fp.SetPosition(V(x, y)); fp.SetOrientationDegrees(rot)
    for pnum, nm in (padnets or {}).items():
        p = fp.FindPadByNumber(str(pnum))
        if p: p.SetNet(net(nm))
        else: raise RuntimeError(f'{ref} missing pad {pnum}')
    board.Add(fp)
    return fp


def add_pad(fp, num, x, y, nm, drill=1.0, dia=2.2, shape=pcbnew.PAD_SHAPE_CIRCLE):
    p = pcbnew.PAD(fp)
    p.SetNumber(str(num)); p.SetPosition(V(x, y)); p.SetSize(pcbnew.VECTOR2I(MM(dia), MM(dia)))
    p.SetDrillSize(pcbnew.VECTOR2I(MM(drill), MM(drill)))
    p.SetShape(shape); p.SetAttribute(pcbnew.PAD_ATTRIB_PTH)
    p.SetLayerSet(pcbnew.LSET.AllCuMask())
    if nm: p.SetNet(net(nm))
    fp.Add(p)
    return p


def make_obd_pigtail(ref='J1'):
    x0, y0 = 12, 16
    fp = pcbnew.FOOTPRINT(board)
    fp.SetReference(ref); fp.SetValue('OBD2_PIGTAIL_16_WIRE_SOLDER_PADS')
    fp.SetFPID(pcbnew.LIB_ID('teensy-41-can-lin', 'OBD2_PigtailPads_Manufacturing'))
    fp.Reference().SetPosition(V(x0, y0-4)); fp.Value().SetPosition(V(x0, y0+41))
    fp.SetPosition(V(0, 0))
    fp.SetLayer(pcbnew.F_Cu)
    # 2 columns x 8 rows, pin numbers match J1962. 1.2 mm drill accepts typical OBD pigtail wires.
    mapping = {
        1: 'OBD1_SINGLE_WIRE_CANDIDATE', 2: 'OBD2_SPARE_PWM_J1850_CANDIDATE',
        3: 'OBD3_CAN_B_PAIR_A_CANDIDATE', 4: 'GND', 5: 'GND',
        6: 'OBD6_CAN_A_PAIR_A', 7: 'OBD7_SINGLE_WIRE_CANDIDATE',
        8: 'OBD8_SINGLE_WIRE_CANDIDATE', 9: 'OBD9_SINGLE_WIRE_CANDIDATE',
        10: 'OBD10_SPARE_PWM_J1850_CANDIDATE', 11: 'OBD11_CAN_B_PAIR_B_CANDIDATE',
        12: 'OBD12_SINGLE_WIRE_CANDIDATE', 13: 'OBD13_SINGLE_WIRE_CANDIDATE',
        14: 'OBD14_CAN_A_PAIR_B', 15: 'OBD15_SINGLE_WIRE_CANDIDATE',
        16: '+12V_OBD',
    }
    for i in range(8):
        add_pad(fp, i+1, x0 + 0, y0 + i*5.0, mapping[i+1], drill=1.2, dia=2.7)
        add_pad(fp, i+9, x0 + 7.5, y0 + i*5.0, mapping[i+9], drill=1.2, dia=2.7)
    # courtyard/fab outline
    for layer in [pcbnew.F_Fab, pcbnew.F_SilkS]:
        for x1,y1,x2,y2 in [(x0-3,y0-3,x0+10.5,y0-3),(x0+10.5,y0-3,x0+10.5,y0+38), (x0+10.5,y0+38,x0-3,y0+38),(x0-3,y0+38,x0-3,y0-3)]:
            s=pcbnew.PCB_SHAPE(fp); s.SetShape(pcbnew.SHAPE_T_SEGMENT); s.SetLayer(layer)
            s.SetStart(V(x1,y1)); s.SetEnd(V(x2,y2)); s.SetWidth(MM(0.12)); fp.Add(s)
    board.Add(fp)
    return fp


def make_teensy_verified(ref='U1'):
    x0, y0 = 118, 15
    fp = pcbnew.FOOTPRINT(board)
    fp.SetReference(ref); fp.SetValue('TEENSY_4.1_MAIN_HEADERS_PJRC_AUDITED')
    fp.SetFPID(pcbnew.LIB_ID('teensy-41-can-lin', 'Teensy_4.1_MainHeaders_PJRC_Audited'))
    fp.Reference().SetPosition(V(x0, y0-4)); fp.Value().SetPosition(V(x0, y0+20))
    fp.SetPosition(V(0, 0)); fp.SetLayer(pcbnew.F_Cu)
    # Front/card view, USB to left. Bottom edge left->right: GND,0..12,3V3,24..32.
    bottom = [('GND_B1','GND'),('0','CAN_B_RX'),('1','CAN_B_TX'),('2',None),('3',None),('4','CAN_B_STB'),('5','CAN_A_STB'),('6','LIN_EN'),('7','LIN_RX'),('8','LIN_TX'),('9',None),('10',None),('11',None),('12',None),('3V3_B','+3V3'),('24',None),('25',None),('26',None),('27',None),('28',None),('29',None),('30',None),('31',None),('32',None)]
    # Top edge left->right: GND,VIN,23..14,3V3,41..33.
    top = [('GND_T1','GND'),('VIN','+5V_REGULATED'),('23','CAN_A_RX'),('22','CAN_A_TX'),('21',None),('20',None),('19',None),('18',None),('17',None),('16',None),('15',None),('14',None),('3V3_T','+3V3'),('41',None),('40',None),('39',None),('38',None),('37',None),('36',None),('35',None),('34',None),('33',None)]
    # Use 0.965 mm finished-hole PJRC guidance; 1.0 mm drill for carrier header holes.
    for i,(num,nm) in enumerate(bottom): add_pad(fp, num, x0 + i*2.54, y0 + 15.24, nm, drill=1.0, dia=1.8)
    for i,(num,nm) in enumerate(top): add_pad(fp, num, x0 + i*2.54, y0 + 0, nm, drill=1.0, dia=1.8)
    # Module body approximation and USB keepout indication.
    for layer in [pcbnew.F_Fab, pcbnew.F_SilkS]:
        for x1,y1,x2,y2 in [(x0-2,y0-2,x0+60.5,y0-2),(x0+60.5,y0-2,x0+60.5,y0+17.3),(x0+60.5,y0+17.3,x0-2,y0+17.3),(x0-2,y0+17.3,x0-2,y0-2)]:
            s=pcbnew.PCB_SHAPE(fp); s.SetShape(pcbnew.SHAPE_T_SEGMENT); s.SetLayer(layer)
            s.SetStart(V(x1,y1)); s.SetEnd(V(x2,y2)); s.SetWidth(MM(0.12)); fp.Add(s)
    board.Add(fp)
    return fp


def edge(x1,y1,x2,y2):
    s=pcbnew.PCB_SHAPE(board); s.SetShape(pcbnew.SHAPE_T_SEGMENT); s.SetLayer(pcbnew.Edge_Cuts)
    s.SetStart(V(x1,y1)); s.SetEnd(V(x2,y2)); s.SetWidth(MM(0.1)); board.Add(s)


def txt(text,x,y,size=1.0,layer=pcbnew.F_SilkS,rot=0):
    t=pcbnew.PCB_TEXT(board); t.SetText(text); t.SetPosition(V(x,y)); t.SetLayer(layer)
    t.SetTextSize(pcbnew.VECTOR2I(MM(size),MM(size))); t.SetTextThickness(MM(0.12)); t.SetTextAngleDegrees(rot)
    board.Add(t); return t

# Board outline with cable pads on left, logic center/right.
W,H=180,105
edge(0,0,W,0); edge(W,0,W,H); edge(W,H,0,H); edge(0,H,0,0)
for ref,x,y in [('MH1',6,6),('MH2',174,6),('MH3',6,99),('MH4',174,99),('SR1',10,60),('SR2',22,66)]:
    add_fp(FP_ROOT/'MountingHole.pretty','MountingHole_3.2mm_M3',ref,'M3' if ref.startswith('MH') else 'CABLE_STRAIN_RELIEF',x,y)

make_obd_pigtail('J1')
make_teensy_verified('U1')

# DIP switch banks.
DIP8='SW_DIP_SPSTx08_Slide_9.78x22.5mm_W7.62mm_P2.54mm'
# SW1 switch pairs: 1-16, 2-15, ... 8-9.
add_fp(FP_ROOT/'Button_Switch_THT.pretty',DIP8,'SW1','CAN_NORMAL_CROSS_DIP_8POS',55,13,0,{
    '1':'OBD6_CAN_A_PAIR_A','16':'CAN_A_H',
    '2':'OBD14_CAN_A_PAIR_B','15':'CAN_A_L',
    '3':'OBD6_CAN_A_PAIR_A','14':'CAN_A_L',
    '4':'OBD14_CAN_A_PAIR_B','13':'CAN_A_H',
    '5':'OBD3_CAN_B_PAIR_A_CANDIDATE','12':'CAN_B_H',
    '6':'OBD11_CAN_B_PAIR_B_CANDIDATE','11':'CAN_B_L',
    '7':'OBD3_CAN_B_PAIR_A_CANDIDATE','10':'CAN_B_L',
    '8':'OBD11_CAN_B_PAIR_B_CANDIDATE','9':'CAN_B_H',
})
add_fp(FP_ROOT/'Button_Switch_THT.pretty',DIP8,'SW2','LIN_K_SOURCE_DIP_8POS_SELECT_ONE',55,52,0,{
    '1':'OBD7_SINGLE_WIRE_CANDIDATE','16':'LIN_BUS',
    '2':'OBD15_SINGLE_WIRE_CANDIDATE','15':'LIN_BUS',
    '3':'OBD1_SINGLE_WIRE_CANDIDATE','14':'LIN_BUS',
    '4':'OBD8_SINGLE_WIRE_CANDIDATE','13':'LIN_BUS',
    '5':'OBD9_SINGLE_WIRE_CANDIDATE','12':'LIN_BUS',
    '6':'OBD12_SINGLE_WIRE_CANDIDATE','11':'LIN_BUS',
    '7':'OBD13_SINGLE_WIRE_CANDIDATE','10':'LIN_BUS',
    '8':'AUX_LIN_K_IO','9':'LIN_BUS',
})

# Transceivers and protection/power.
add_fp(FP_ROOT/'Package_SO.pretty','SOIC-8_3.9x4.9mm_P1.27mm','U2','TJA1051_CAN_A',94,18,0,{
    '1':'CAN_A_TX','2':'GND','3':'+5V_REGULATED','4':'CAN_A_RX','6':'CAN_A_L','7':'CAN_A_H','8':'CAN_A_STB'})
add_fp(FP_ROOT/'Package_SO.pretty','SOIC-8_3.9x4.9mm_P1.27mm','U3','TJA1051_CAN_B',94,39,0,{
    '1':'CAN_B_TX','2':'GND','3':'+5V_REGULATED','4':'CAN_B_RX','6':'CAN_B_L','7':'CAN_B_H','8':'CAN_B_STB'})
add_fp(FP_ROOT/'Package_SO.pretty','SOIC-8_3.9x4.9mm_P1.27mm','U4','TJA1021_LIN_K_VERIFY_PROTOCOL',94,64,0,{
    '1':'LIN_TX','2':'GND','3':'+5V_REGULATED','4':'LIN_RX','6':'LIN_BUS','7':'LIN_EN','8':'+12V_PROTECTED'})
add_fp(FP_ROOT/'Fuse.pretty','Fuse_1206_3216Metric','F1','POLYFUSE_500mA',30,72,0,{'1':'+12V_OBD','2':'+12V_PROTECTED'})
add_fp(FP_ROOT/'Diode_SMD.pretty','D_SMA','D1','SMBJ24CA_TVS_12V',24,84,0,{'1':'+12V_PROTECTED','2':'GND'})
add_fp(FP_ROOT/'Package_TO_SOT_SMD.pretty','TO-263-5_TabPin3','U5','LM2596S-5_BUCK_VERIFY_BOM',42,88,0,{'1':'+12V_PROTECTED','2':'+5V_REGULATED','3':'GND','4':'+5V_REGULATED','5':'GND'})

# Auxiliary header for bench/cable expansion.
add_fp(FP_ROOT/'Connector_PinHeader_2.54mm.pretty','PinHeader_1x08_P2.54mm_Vertical','J2','AUX_HEADER',158,62,0,{
    '1':'CAN_B_H','2':'CAN_B_L','3':'AUX_LIN_K_IO','4':'GND','5':'+5V_REGULATED','6':'+12V_PROTECTED','7':'CAN_A_H','8':'CAN_A_L'})

# Test pads.
for ref,val,x,y,nm in [
    ('TP1','12V',34,60,'+12V_OBD'),('TP2','5V',44,60,'+5V_REGULATED'),('TP3','GND',24,60,'GND'),
    ('TP4','CAN_A_H',111,18,'CAN_A_H'),('TP5','CAN_A_L',111,24,'CAN_A_L'),
    ('TP6','CAN_B_H',111,39,'CAN_B_H'),('TP7','CAN_B_L',111,45,'CAN_B_L'),
    ('TP8','LIN_BUS',111,64,'LIN_BUS'),('TP9','AUX_LIN_K',158,88,'AUX_LIN_K_IO')]:
    add_fp(FP_ROOT/'TestPoint.pretty','TestPoint_Pad_D1.5mm',ref,val,x,y,0,{'1':nm})

# Readable manufacturing/configuration labels. Use Cmts for detailed warnings to avoid silk DRC clutter.
txt('R5 OBD PIGTAIL + DIP SWITCH CAN/LIN INTERFACE',35,4,1.0,pcbnew.F_SilkS)
txt('J1: solder OBD cable wires by pin number. Use SR holes for zip-tie strain relief.',4,66,0.75,pcbnew.Cmts_User)
txt('SW1 CAN: 1+2=A normal, 3+4=A cross, 5+6=B normal, 7+8=B cross. Never normal+cross together.',42,42,0.75,pcbnew.Cmts_User)
txt('SW2 LIN/K: select exactly ONE source. LIN/K is single-wire; no polarity reversal.',42,81,0.75,pcbnew.Cmts_User)
txt('Teensy pins audited vs PJRC: CAN1=22/23, CAN2=1/0, LIN UART=8/7.',104,92,0.75,pcbnew.Cmts_User)
txt('OBD PIGTAIL PADS',15,9,0.8,pcbnew.F_SilkS)
# Compact OBD pad labels on comments layer, not silk.
labels=[('1',2,16),('2',2,21),('3',2,26),('4G',2,31),('5G',2,36),('6A',2,41),('7K',2,46),('8',2,51),('9',21,16),('10',21,21),('11B',21,26),('12',21,31),('13',21,36),('14A',21,41),('15L',21,46),('16+',21,51)]
for s,x,y in labels: txt(s,x,y,0.65,pcbnew.Cmts_User)

# Board setup: modest automotive prototype clearances/tracks.
ds = board.GetDesignSettings()
try:
    ds.SetSmallestClearanceValue(MM(0.2))
except AttributeError:
    pass

pcbnew.SaveBoard(str(OUT), board)
# Save generated custom footprints into the project local library so KiCad DRC/library checks resolve them.
lib_dir = PROJECT / 'teensy-41-can-lin.pretty'
lib_dir.mkdir(exist_ok=True)
for ref in ('J1', 'U1'):
    fp = board.FindFootprintByReference(ref)
    if fp:
        pcbnew.FootprintSave(str(lib_dir), fp)
for ext in ['.kicad_pro','.kicad_prl']:
    src=PROJECT/f'teensy-41-can-lin-r4-universal-routing-matrix{ext}'
    dst=PROJECT/f'teensy-41-can-lin-r5-pigtail-dipswitch{ext}'
    if src.exists(): dst.write_text(src.read_text())
print('saved', OUT, OUT.stat().st_size)
