from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.holdtap import HoldTap
from kmk.hid import HIDModes
from kmk.handlers.sequences import send_string
import supervisor
from kmk.extensions.peg_oled_display import Oled,OledDisplayMode,OledReactionType,OledData
from kmk.extensions.peg_rgb_matrix import Rgb_matrix
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.extensions.media_keys import MediaKeys
keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())
modtap = ModTap()
layers_ext = Layers()
holdTap = HoldTap()
# oled
oled_ext = Oled(OledData(corner_one={0:OledReactionType.STATIC,1:["1 2 3 4 5 6","","","","","","",""]},corner_two={0:OledReactionType.STATIC,1:[" 7 8 Layer","","","","","",""," 7 8 Layer"]},corner_three={0:OledReactionType.LAYER,1:["^","  ^","    ^","      ^","        ^","          ^","",""]},corner_four={0:OledReactionType.LAYER,1:["","","","","",""," ^","   ^"]}),toDisplay=OledDisplayMode.TXT,flip= True)
# oled
keyboard.extensions.append(oled_ext)
# ledmap
rgb_ext = Rgb_matrix(ledDisplay=[[255,55,55],[55,55,55],[55,55,55],[55,55,55],[55,55,55],[18,209,123],[255,0,0],[55,55,55],[55,55,55],[55,55,55],[55,55,55],[255,55,55],[255,55,55],[55,55,55],[0,255,217],[0,255,217],[0,255,217],[255,0,0],[0,255,217],[0,255,217],[0,255,217],[0,255,217],[55,55,55],[255,55,55],[255,55,55],[55,55,55],[55,55,55],[55,55,55],[55,55,55],[0,25,255],[0,25,255],[255,0,0],[255,0,0],[0,255,77],[55,55,55],[255,55,55],[255,55,55],[55,55,55],[0,255,77],[0,25,255],[0,255,77],[255,55,55],[0,0,55],[0,0,55],[0,0,55],[0,0,55],[0,0,55],[0,0,55],[0,0,55],[0,0,55],[0,0,55],[0,0,55],[0,0,55],[0,0,0]],split=True,rightSide=False,disable_auto_write=True)
# ledmap
keyboard.extensions.append(rgb_ext)
# TODO Comment one of these on each side
split_side = SplitSide.LEFT
#split_side = SplitSide.RIGHT
split = Split(use_pio=True)
keyboard.modules = [layers_ext, modtap, split, holdTap]

LSPACE = KC.HT(KC.SPACE, KC.MO(1))
RSPACE = KC.HT(KC.SPACE, KC.MO(2))
# keymap
keyboard.keymap = [
    [
        KC.ESCAPE,          KC.Q,       KC.W,           KC.E,       KC.R,   KC.T,           KC.Y,   KC.U,       KC.I,       KC.O,       KC.P,       KC.BSPC,
        KC.TAB,             KC.A,       KC.S,           KC.D,       KC.F,   KC.G,           KC.H,   KC.J,       KC.K,       KC.L,       KC.SCOLON,  KC.QUOTE,
        KC.LSHIFT,          KC.Z,       KC.X,           KC.C,       KC.V,   KC.B,           KC.N,   KC.M,       KC.COMMA,   KC.DOT,     KC.SLASH,   KC.ENTER,
                                                        KC.NO,      KC.NO,  LSPACE,         RSPACE, KC.BSPC,    KC.DELETE,  
        KC.RALT,    KC.NO
    ],

    [   KC.NO,      KC.NO,      KC.AT,          KC.HASH,    KC.NO,      KC.NO,          KC.NO,    KC.NO,      KC.NO,     KC.NO,      KC.NO,      KC.BSPC,
        KC.NO,      KC.NO,      KC.LALT,        KC.LCTRL,   KC.LSHIFT,  KC.NO,          KC.LEFT,  KC.DOWN,    KC.UP,     KC.RIGHT,   KC.PIPE,    KC.NO,
        KC.NO,      KC.NO,      KC.NO,          KC.NO,      KC.NO,      KC.NO,          KC.HOME,  KC.PLUS,    KC.NO,     KC.END,     KC.NO,      KC.NO,
                                                KC.NO,      KC.NO,      KC.NO,          KC.NO,    KC.BSPC,    KC.DELETE,  

        KC.RALT,    KC.NO
     ],
    [
        KC.NO,      KC.LBRACKET,      KC.N7,          KC.N8,      KC.N9,  KC.RBRACKET,          KC.NO,  KC.NO,          KC.NO,     KC.NO,      KC.NO,      KC.BSPC,
        KC.NO,      KC.SCOLON,        KC.N4,          KC.N5,      KC.N6,  KC.EQUAL,             KC.NO,  KC.LSHIFT,      KC.LCTRL,  KC.LALT,    KC.NO,      KC.NO,
        KC.NO,      KC.GRAVE,         KC.N1,          KC.N2,      KC.N3,  KC.BSLASH,            KC.NO,  KC.PLUS,        KC.NO,     KC.NO,      KC.NO,      KC.NO,
                                                      KC.DOT,     KC.N0,  KC.MINUS,             KC.NO,  KC.NO,          KC.NO,

        KC.RALT,    KC.NO
    ],
    [
        KC.NO,      KC.NO,      KC.NO,          KC.NO,      KC.NO,  KC.NO,          KC.NO,  KC.NO,      KC.NO,  KC.NO,      KC.NO,      KC.NO,
        KC.NO,      KC.NO,      KC.NO,          KC.NO,      KC.NO,  KC.NO,          KC.NO,  KC.NO,      KC.NO,  KC.NO,      KC.NO,      KC.NO,
        KC.NO,      KC.NO,      KC.NO,          KC.NO,      KC.NO,  KC.NO,          KC.NO,  KC.NO,      KC.NO,  KC.NO,      KC.NO,      KC.NO,
                                                KC.NO,      KC.NO,  KC.NO,          KC.NO,  KC.NO,      KC.NO,  KC.NO,
        KC.RALT,KC.NO
    ],
    [       
        KC.MO(1),   KC.MO(2),   KC.RGB_TOG,     KC.E,       KC.R,   KC.T,           KC.Y,   KC.U,       KC.I,   KC.O,       KC.P,       KC.BSPC,
        KC.ENTER,   KC.A,       KC.S,           KC.D,       KC.F,   KC.G,           KC.H,   KC.J,       KC.K,   KC.L,       KC.NO,      KC.NO,
        KC.NO,      KC.Z,       KC.X,           KC.C,       KC.V,   KC.B,           KC.N,   KC.M,       KC.NO,  KC.DOT,     KC.NO,      KC.NO,
                                                KC.NO,      KC.NO,  KC.NO,          KC.NO,  KC.NO,      KC.NO,  
        KC.RALT,    KC.NO
    ],
    [
        KC.NO,      KC.NO,      KC.AT,          KC.HASH,    KC.NO,  KC.NO,          KC.NO,  KC.NO,      KC.NO,  KC.NO,      KC.NO,      KC.BSPC,
        KC.NO,      KC.NO,      KC.NO,          KC.NO,      KC.NO,  KC.NO,          KC.NO,  KC.NO,      KC.NO,  KC.NO,      KC.PIPE,    KC.NO,
        KC.NO,      KC.NO,      KC.NO,          KC.NO,      KC.NO,  KC.NO,          KC.NO,  KC.PLUS,    KC.NO,  KC.NO,      KC.NO,      KC.NO,
                                                KC.NO,      KC.NO,  KC.NO,          KC.NO,  KC.NO,      KC.NO,
        KC.RALT,KC.NO
    ], 
    [
        KC.NO,      KC.NO,      KC.AT,          KC.HASH,    KC.NO,  KC.NO,          KC.NO,  KC.NO,      KC.NO,  KC.NO,      KC.NO,      KC.BSPC,
        KC.NO,      KC.NO,      KC.NO,          KC.NO,      KC.NO,  KC.NO,          KC.NO,  KC.NO,      KC.NO,  KC.NO,      KC.PIPE,    KC.NO,
        KC.NO,      KC.NO,      KC.NO,          KC.NO,      KC.NO,  KC.NO,          KC.NO,  KC.PLUS,    KC.NO,  KC.NO,      KC.NO,      KC.NO,
                                                KC.NO,      KC.NO,  KC.NO,          KC.NO,  KC.NO,      KC.NO,
        KC.RALT,KC.NO
    ],
    [
        KC.NO,      KC.NO,      KC.NO,          KC.NO,      KC.NO,  KC.NO,          KC.NO,  KC.NO,      KC.NO,  KC.NO,      KC.NO,      KC.NO,
        KC.NO,      KC.NO,      KC.NO,          KC.NO,      KC.NO,  KC.NO,          KC.NO,  KC.NO,      KC.NO,  KC.NO,      KC.NO,      KC.NO,
        KC.NO,      KC.NO,      KC.NO,          KC.NO,      KC.NO,  KC.NO,          KC.NO,  KC.NO,      KC.NO,  KC.NO,      KC.NO,      KC.NO,
                                                KC.NO,      KC.NO,  KC.NO,          KC.NO,  KC.NO,      KC.NO,  KC.NO,
        KC.RALT,KC.NO
    ] 
]
# keymap
if __name__ == '__main__':
    keyboard.go(hid_type=HIDModes.USB)