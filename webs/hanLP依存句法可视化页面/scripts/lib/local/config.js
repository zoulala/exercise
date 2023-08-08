// -*- Mode: JavaScript; tab-width: 4; indent-tabs-mode: nil; -*-
// vim:set ft=javascript ts=4 sw=4 sts=4 cindent:

var Config = (function (window, undefined) {

    var bratCollData = {
        'entity_types': [
// this is optional
            {
                'type': 'SPAN_DEFAULT',
                'bgColor': '#7fa2ff',
                'borderColor': 'darken'
            },
            {
                'type': 'Ag',
                'bgColor': '#ff3721',
                'borderColor': 'darken'
            },
            {
                'type': 'Bg',
                'bgColor': '#01ff75',
                'borderColor': 'darken'
            },
            {
                'type': 'Dg',
                'bgColor': '#6d94ff',
                'borderColor': 'darken'
            },
            {
                'type': 'Mg',
                'bgColor': '#77ff32',
                'borderColor': 'darken'
            },
            {
                'type': 'Ng',
                'bgColor': '#ffb3b4',
                'borderColor': 'darken'
            },
            {
                'type': 'PART',
                'bgColor': '#ffb3b4',
                'borderColor': 'darken'
            },
            {
                'type': 'Rg',
                'bgColor': '#ff4b3d',
                'borderColor': 'darken'
            },
            {
                'type': 'PRON',
                'bgColor': '#ff79bc',
                'borderColor': 'darken'
            },
            {
                'type': 'PRP$',
                'bgColor': '#ffec68',
                'borderColor': 'darken'
            },
            {
                'type': 'PRP',
                'bgColor': '#eaff7c',
                'borderColor': 'darken'
            },
            {
                'type': 'WP',
                'bgColor': '#f3c8ff',
                'borderColor': 'darken'
            },
            {
                'type': 'Tg',
                'bgColor': '#ff57ec',
                'borderColor': 'darken'
            },
            {
                'type': 'Vg',
                'bgColor': '#ff82db',
                'borderColor': 'darken'
            },
            {
                'type': 'Yg',
                'bgColor': '#c126ff',
                'borderColor': 'darken'
            },
            {
                'type': 'a',
                'bgColor': '#e5ff6c',
                'borderColor': 'darken'
            },
            {
                'type': 'ADJ',
                'bgColor': '#e5ff6c',
                'borderColor': 'darken'
            },
            {
                'type': 'VA',
                'bgColor': '#e5ff6c',
                'borderColor': 'darken'
            },
            {
                'type': 'VC',
                'bgColor': '#85ffd0',
                'borderColor': 'darken'
            },
            {
                'type': 'DATE',
                'bgColor': '#85ffd0',
                'borderColor': 'darken'
            },
            {
                'type': 'TIME',
                'bgColor': '#6affe9',
                'borderColor': 'darken'
            },
            {
                'type': 'VE',
                'bgColor': '#89f8ff',
                'borderColor': 'darken'
            },
            {
                'type': 'AUX',
                'bgColor': '#89f8ff',
                'borderColor': 'darken'
            },
            {
                'type': 'ad',
                'bgColor': '#7ccfff',
                'borderColor': 'darken'
            },
            {
                'type': 'ADV',
                'bgColor': '#7ccfff',
                'borderColor': 'darken'
            },
            {
                'type': 'AD',
                'bgColor': '#7ccfff',
                'borderColor': 'darken'
            },

            {
                'type': 'an',
                'bgColor': '#67ffcd',
                'borderColor': 'darken'
            },
            {
                'type': 'b',
                'bgColor': '#5af2f1',
                'borderColor': 'darken'
            },
            {
                'type': 'c',
                'bgColor': '#e4deff',
                'borderColor': 'darken'
            },
            {
                'type': 'CC',
                'bgColor': '#e4deff',
                'borderColor': 'darken'
            },
            {
                'type': 'CCONJ',
                'bgColor': '#e4deff',
                'borderColor': 'darken'
            },
            {
                'type': 'CS',
                'bgColor': '#d3e2ff',
                'borderColor': 'darken'
            },
            {
                'type': 'SCONJ',
                'bgColor': '#d3e2ff',
                'borderColor': 'darken'
            },
            {
                'type': 'd',
                'bgColor': '#ff9de4',
                'borderColor': 'darken'
            },
            {
                'type': 'e',
                'bgColor': '#b4b4ff',
                'borderColor': 'darken'
            },
            {
                'type': 'SP',
                'bgColor': '#b4b4ff',
                'borderColor': 'darken'
            },
            {
                'type': 'IJ',
                'bgColor': '#95d0ff',
                'borderColor': 'darken'
            },
            {
                'type': 'ON',
                'bgColor': '#6ddaff',
                'borderColor': 'darken'
            },
            {
                'type': 'f',
                'bgColor': '#27f4b7',
                'borderColor': 'darken'
            },
            {
                'type': 'LC',
                'bgColor': '#27f4b7',
                'borderColor': 'darken'
            },
            {
                'type': 'h',
                'bgColor': '#f2ff1b',
                'borderColor': 'darken'
            },
            {
                'type': 'LAW',
                'bgColor': '#f2ff1b',
                'borderColor': 'darken'
            },
            {
                'type': 'i',
                'bgColor': '#cccdff',
                'borderColor': 'darken'
            },
            {
                'type': 'j',
                'bgColor': '#28c163',
                'borderColor': 'darken'
            },
            {
                'type': 'k',
                'bgColor': '#9695ff',
                'borderColor': 'darken'
            },
            {
                'type': 'l',
                'bgColor': '#ff9ef5',
                'borderColor': 'darken'
            },
            {
                'type': 'WORK_OF_ART',
                'bgColor': '#ff9ef5',
                'borderColor': 'darken'
            },
            {
                'type': 'm',
                'bgColor': '#cdff00',
                'borderColor': 'darken'
            },
            {
                'type': 'PERCENT',
                'bgColor': '#cdff00',
                'borderColor': 'darken'
            },
            {
                'type': 'ORDINAL',
                'bgColor': '#c3ff65',
                'borderColor': 'darken'
            },
            {
                'type': 'CARDINAL',
                'bgColor': '#bcff8b',
                'borderColor': 'darken'
            },
            {
                'type': 'QUANTITY',
                'bgColor': '#d1ff3f',
                'borderColor': 'darken'
            },
            {
                'type': 'MONEY',
                'bgColor': '#f8ff85',
                'borderColor': 'darken'
            },
            {
                'type': 'NUM',
                'bgColor': '#cdff00',
                'borderColor': 'darken'
            },
            {
                'type': 'EVENT',
                'bgColor': '#cdff00',
                'borderColor': 'darken'
            },
            {
                'type': 'OD',
                'bgColor': '#f3ffb6',
                'borderColor': 'darken'
            },
            {
                'type': 'M',
                'bgColor': '#fff4d2',
                'borderColor': 'darken'
            },
            {
                'type': 'n',
                'bgColor': '#12fffc',
                'borderColor': 'darken'
            },
            {
                'type': 'NOUN',
                'bgColor': '#12fffc',
                'borderColor': 'darken'
            },
            {
                'type': 'JJ',
                'bgColor': '#eaff7c',
                'borderColor': 'darken'
            },
            {
                'type': 'NN',
                'bgColor': '#12fffc',
                'borderColor': 'darken'
            },
            {
                'type': 'nr',
                'bgColor': '#fffdc3',
                'borderColor': 'darken'
            },
            {
                'type': 'PERSON',
                'bgColor': '#fffdc3',
                'borderColor': 'darken'
            },
            {
                'type': '人名',
                'bgColor': '#fffdc3',
                'borderColor': 'darken'
            },
            {
                'type': 'ns',
                'bgColor': '#ffc4cc',
                'borderColor': 'darken'
            },
            {
                'type': '地名',
                'bgColor': '#ffc4cc',
                'borderColor': 'darken'
            },
            {
                'type': 'LOCATION',
                'bgColor': '#ffc4cc',
                'borderColor': 'darken'
            },
            {
                'type': 'nt',
                'bgColor': '#4fffa8',
                'borderColor': 'darken'
            },
            {
                'type': '机构团体',
                'bgColor': '#4fffa8',
                'borderColor': 'darken'
            },
            {
                'type': 'ORGANIZATION',
                'bgColor': '#4fffa8',
                'borderColor': 'darken'
            },
            {
                'type': 'nx',
                'bgColor': '#c98dff',
                'borderColor': 'darken'
            },
            {
                'type': 'SYM',
                'bgColor': '#c98dff',
                'borderColor': 'darken'
            },
            {
                'type': 'NORP',
                'bgColor': '#c98dff',
                'borderColor': 'darken'
            },
            {
                'type': 'nz',
                'bgColor': '#05ccff',
                'borderColor': 'darken'
            },
            {
                'type': 'PRODUCT',
                'bgColor': '#05ccff',
                'borderColor': 'darken'
            },
            {
                'type': 'NR',
                'bgColor': '#05ccff',
                'borderColor': 'darken'
            },
            {
                'type': 'NNP',
                'bgColor': '#05ccff',
                'borderColor': 'darken'
            },
            {
                'type': 'PROPN',
                'bgColor': '#05ccff',
                'borderColor': 'darken'
            },
            {
                'type': 'o',
                'bgColor': '#fff6bf',
                'borderColor': 'darken'
            },
            {
                'type': 'p',
                'bgColor': '#94caff',
                'borderColor': 'darken'
            },
            {
                'type': 'ADP',
                'bgColor': '#94caff',
                'borderColor': 'darken'
            },
            {
                'type': 'P',
                'bgColor': '#94caff',
                'borderColor': 'darken'
            },
            {
                'type': 'IN',
                'bgColor': '#94caff',
                'borderColor': 'darken'
            },
            {
                'type': 'LB',
                'bgColor': '#d2ff9b',
                'borderColor': 'darken'
            },
            {
                'type': 'SB',
                'bgColor': '#ddff63',
                'borderColor': 'darken'
            },
            {
                'type': 'FACILITY',
                'bgColor': '#ddff63',
                'borderColor': 'darken'
            },
            {
                'type': 'BA',
                'bgColor': '#cbffb8',
                'borderColor': 'darken'
            },
            {
                'type': 'q',
                'bgColor': '#76d9f2',
                'borderColor': 'darken'
            },
            {
                'type': 'r',
                'bgColor': '#37ff10',
                'borderColor': 'darken'
            },
            {
                'type': 'PN',
                'bgColor': '#37ff10',
                'borderColor': 'darken'
            },
            {
                'type': 'DT',
                'bgColor': '#15ffa0',
                'borderColor': 'darken'
            },
            {
                'type': 'DET',
                'bgColor': '#15ffa0',
                'borderColor': 'darken'
            },
            {
                'type': 's',
                'bgColor': '#ffb973',
                'borderColor': 'darken'
            },
            {
                'type': 'INTJ',
                'bgColor': '#ffb973',
                'borderColor': 'darken'
            },
            {
                'type': 't',
                'bgColor': '#d1fffb',
                'borderColor': 'darken'
            },
            {
                'type': 'NT',
                'bgColor': '#d1fffb',
                'borderColor': 'darken'
            },
            {
                'type': 'u',
                'bgColor': '#d3b9ff',
                'borderColor': 'darken'
            },
            {
                'type': 'ETC',
                'bgColor': '#f3c8ff',
                'borderColor': 'darken'
            },
            {
                'type': 'MSP',
                'bgColor': '#ffc1fa',
                'borderColor': 'darken'
            },
            {
                'type': 'DEG',
                'bgColor': '#bf9aff',
                'borderColor': 'darken'
            },
            {
                'type': 'DEC',
                'bgColor': '#a9b0ff',
                'borderColor': 'darken'
            },
            {
                'type': 'DER',
                'bgColor': '#8f99ff',
                'borderColor': 'darken'
            },
            {
                'type': 'DEV',
                'bgColor': '#9482ff',
                'borderColor': 'darken'
            },
            {
                'type': 'AS',
                'bgColor': '#a971ff',
                'borderColor': 'darken'
            },
            {
                'type': 'v',
                'bgColor': '#bde7ff',
                'borderColor': 'darken'
            },
            {
                'type': 'VV',
                'bgColor': '#bde7ff',
                'borderColor': 'darken'
            },
            {
                'type': 'VBZ',
                'bgColor': '#bde7ff',
                'borderColor': 'darken'
            },
            {
                'type': 'VBD',
                'bgColor': '#a8d5ef',
                'borderColor': 'darken'
            },
            {
                'type': 'VERB',
                'bgColor': '#bde7ff',
                'borderColor': 'darken'
            },
            {
                'type': 'vd',
                'bgColor': '#a6fc50',
                'borderColor': 'darken'
            },
            {
                'type': 'vn',
                'bgColor': '#c6b0ff',
                'borderColor': 'darken'
            },
            {
                'type': 'w',
                'bgColor': '#d3ffdc',
                'borderColor': 'darken'
            },
            {
                'type': 'PU',
                'bgColor': '#d3ffdc',
                'borderColor': 'darken'
            },
            {
                'type': 'PUNCT',
                'bgColor': '#d3ffdc',
                'borderColor': 'darken'
            },
            {
                'type': 'x',
                'bgColor': '#ff4bee',
                'borderColor': 'darken'
            },
            {
                'type': 'X',
                'bgColor': '#ff4bee',
                'borderColor': 'darken'
            },
            {
                'type': 'FW',
                'bgColor': '#ff4bee',
                'borderColor': 'darken'
            },
            {
                'type': 'y',
                'bgColor': '#b2ffa8',
                'borderColor': 'darken'
            },
            {
                'type': 'z',
                'bgColor': '#77ffff',
                'borderColor': 'darken'
            },
            {
                'type': 'ARC_DEFAULT',
                'color': 'black',
                'arrowHead': 'triangle,5',
                'labelArrow': 'triangle,3,5',
            },
            {
                'type': 'token',
                'labels': ['\u00A0\u00A0'], // non-breaking space for empty
            },
            {
                'type': '-',
                'labels': ['\u00A0\u00A0'], // non-breaking space for empty
            }
        ],
        'event_attribute_types': [],
        'entity_attribute_types': [
            {
                'type': 'Name',
                'values': {
                    'Name': {'glyph': '(N)'},
                },
            },
        ],
        'relation_types': [
// this is optional
//         {
//             'type': 'subj',
//             'labels': [ 'subj' ],
//             'dashArray': '3,3',
//             'color': 'green',
//             'args': [
//                 {
//                     'role': 'arg1',
//                     'targets': [ 'token' ]
//                 },
//                 {
//                     'role': 'arg2',
//                     'targets': [ 'token' ]
//                 }
//             ]
//         }
        ],
        'event_types': [],
    };

    return {
        bratCollData: bratCollData,
    };
})(window);
