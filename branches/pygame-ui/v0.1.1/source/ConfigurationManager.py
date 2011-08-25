#!/usr/bin/env python

# 	=============================== Configuration Manager =================================
#
#	AUTHOR: KONSTANTIN DINEV
#	DATE: July 2011
#	DESCRIPTION: Configuration manager designed for pygame-ui component framework. This
#		manager takes xml configuration for components and initializes styling and other
#		framework configurations
#	CONDITIONS: Used by the BaseUIComponent class to initialize individual component 
#		styling
#	VISION: Initial precondition for designer and design time development
#   PROJECT BY: http://www.sarconsrealm.org
#	
#	=======================================================================================
from xml.dom.minidom import parse
import pygame

COLOR = {
'air force blue' : '#5D8AA8', 
'alice blue' : '#F0F8FF', 
'alizarin crimson' : '#E32636', 
'almond' : '#EFDECD', 
'amaranth' : '#E52B50', 
'amber' : '#FFBF00', 
'american rose' : '#FF033E', 
'amethyst' : '#9966CC', 
'android green' : '#A4C639', 
'anti-flash white' : '#F2F3F4', 
'antique brass' : '#CD9575', 
'antique fuchsia' : '#915C83', 
'antique white' : '#FAEBD7', 
'ao (english)' : '#008000', 
'apple green' : '#8DB600', 
'apricot' : '#FBCEB1', 
'aqua' : '#00FFFF', 
'aquamarine' : '#7FFFD4', 
'army green' : '#4B5320', 
'arsenic' : '#3B444B', 
'arylide yellow' : '#E9D66B', 
'ash grey' : '#B2BEB5', 
'asparagus' : '#87A96B', 
'atomic tangerine' : '#FF9966', 
'auburn' : '#A52A2A', 
'aureolin' : '#FDEE00', 
'aurometalsaurus' : '#6E7F80', 
'awesome' : '#FF2052', 
'azure' : '#007FFF', 
'azure mist/web' : '#F0FFFF', 
'baby blue' : '#89CFF0', 
'baby blue eyes' : '#A1CAF1', 
'baby pink' : '#F4C2C2', 
'ball blue' : '#21ABCD', 
'banana mania' : '#FAE7B5', 
'banana yellow' : '#FFE135', 
'battleship grey' : '#848482', 
'bazaar' : '#98777B', 
'beau blue' : '#BCD4E6', 
'beaver' : '#9F8170', 
'beige' : '#F5F5DC', 
'bisque' : '#FFE4C4', 
'bistre' : '#3D2B1F', 
'bittersweet' : '#FE6F5E', 
'black' : '#000000', 
'blanched almond' : '#FFEBCD', 
'bleu de france' : '#318CE7', 
'blizzard blue' : '#ACE5EE', 
'blond' : '#FAF0BE', 
'blue' : '#0000FF', 
'blue (munsell)' : '#0093AF', 
'blue (ncs)' : '#0087BD', 
'blue (pigment)' : '#333399', 
'blue (ryb)' : '#0247FE', 
'blue bell' : '#A2A2D0', 
'blue gray' : '#6699CC', 
'blue-green' : '#00DDDD', 
'blue-violet' : '#8A2BE2', 
'blush' : '#DE5D83', 
'bole' : '#79443B', 
'bondi blue' : '#0095B6', 
'boston university red' : '#CC0000', 
'brandeis blue' : '#0070FF', 
'brass' : '#B5A642', 
'brick red' : '#CB4154', 
'bright cerulean' : '#1DACD6', 
'bright green' : '#66FF00', 
'bright lavender' : '#BF94E4', 
'bright maroon' : '#C32148', 
'bright pink' : '#FF007F', 
'bright turquoise' : '#08E8DE', 
'bright ube' : '#D19FE8', 
'brilliant lavender' : '#F4BBFF', 
'brilliant rose' : '#FF55A3', 
'brink pink' : '#FB607F', 
'british racing green' : '#004225', 
'bronze' : '#CD7F32', 
'brown (traditional)' : '#964B00', 
'brown (web)' : '#A52A2A', 
'bubble gum' : '#FFC1CC', 
'bubbles' : '#E7FEFF', 
'buff' : '#F0DC82', 
'bulgarian rose' : '#480607', 
'burgundy' : '#800020', 
'burlywood' : '#DEB887', 
'burnt orange' : '#CC5500', 
'burnt sienna' : '#E97451', 
'burnt umber' : '#8A3324', 
'byzantine' : '#BD33A4', 
'byzantium' : '#702963', 
'cadet' : '#536872', 
'cadet blue' : '#5F9EA0', 
'cadet grey' : '#91A3B0', 
'cadmium green' : '#006B3C', 
'cadmium orange' : '#ED872D', 
'cadmium red' : '#E30022', 
'cadmium yellow' : '#FFF600', 
'café au lait' : '#A67B5B', 
'café noir' : '#4B3621', 
'cal poly pomona green' : '#1E4D2B', 
'cambridge blue' : '#A3C1AD', 
'camel' : '#C19A6B', 
'camouflage green' : '#78866B', 
'canary yellow' : '#FFEF00', 
'candy apple red' : '#FF0800', 
'candy pink' : '#E4717A', 
'capri' : '#00BFFF', 
'caput mortuum' : '#592720', 
'cardinal' : '#C41E3A', 
'caribbean green' : '#00CC99', 
'carmine' : '#960018', 
'carmine pink' : '#EB4C42', 
'carmine red' : '#FF0038', 
'carnation pink' : '#FFA6C9', 
'carnelian' : '#B31B1B', 
'carolina blue' : '#99BADD', 
'carrot orange' : '#ED9121', 
'ceil' : '#92A1CF', 
'celadon' : '#ACE1AF', 
'celestial blue' : '#4997D0', 
'cerise' : '#DE3163', 
'cerise pink' : '#EC3B83', 
'cerulean' : '#007BA7', 
'cerulean blue' : '#2A52BE', 
'cg blue' : '#007AA5', 
'cg red' : '#E03C31', 
'chamoisee' : '#A0785A', 
'champagne' : '#F7E7CE', 
'charcoal' : '#36454F', 
'chartreuse (traditional)' : '#DFFF00', 
'chartreuse (web)' : '#7FFF00', 
'cherry blossom pink' : '#FFB7C5', 
'chestnut' : '#CD5C5C', 
'chocolate (traditional)' : '#7B3F00', 
'chocolate (web)' : '#D2691E', 
'chrome yellow' : '#FFA700', 
'cinereous' : '#98817B', 
'cinnabar' : '#E34234', 
'cinnamon' : '#D2691E', 
'citrine' : '#E4D00A', 
'classic rose' : '#FBCCE7', 
'cobalt' : '#0047AB', 
'cocoa brown' : '#D2691E', 
'coffee' : '#6F4E37', 
'columbia blue' : '#9BDDFF', 
'cool black' : '#002E63', 
'cool grey' : '#8C92AC', 
'copper' : '#B87333', 
'copper rose' : '#996666', 
'coquelicot' : '#FF3800', 
'coral' : '#FF7F50', 
'coral pink' : '#F88379', 
'coral red' : '#FF4040', 
'cordovan' : '#893F45', 
'corn' : '#FBEC5D', 
'cornell red' : '#B31B1B', 
'cornflower blue' : '#6495ED', 
'cornsilk' : '#FFF8DC', 
'cosmic latte' : '#FFF8E7', 
'cotton candy' : '#FFBCD9', 
'cream' : '#FFFDD0', 
'crimson' : '#DC143C', 
'crimson glory' : '#BE0032', 
'cyan' : '#00FFFF', 
'cyan (process)' : '#00B7EB', 
'daffodil' : '#FFFF31', 
'dandelion' : '#F0E130', 
'dark blue' : '#00008B', 
'dark brown' : '#654321', 
'dark byzantium' : '#5D3954', 
'dark candy apple red' : '#A40000', 
'dark cerulean' : '#08457E', 
'dark champagne' : '#C2B280', 
'dark chestnut' : '#986960', 
'dark coral' : '#CD5B45', 
'dark cyan' : '#008B8B', 
'dark electric blue' : '#536878', 
'dark goldenrod' : '#B8860B', 
'dark gray' : '#A9A9A9', 
'dark green' : '#013220', 
'dark jungle green' : '#1A2421', 
'dark khaki' : '#BDB76B', 
'dark lava' : '#483C32', 
'dark lavender' : '#734F96', 
'dark magenta' : '#8B008B', 
'dark midnight blue' : '#003366', 
'dark olive green' : '#556B2F', 
'dark orange' : '#FF8C00', 
'dark orchid' : '#9932CC', 
'dark pastel blue' : '#779ECB', 
'dark pastel green' : '#03C03C', 
'dark pastel purple' : '#966FD6', 
'dark pastel red' : '#C23B22', 
'dark pink' : '#E75480', 
'dark powder blue' : '#003399', 
'dark raspberry' : '#872657', 
'dark red' : '#8B0000', 
'dark salmon' : '#E9967A', 
'dark scarlet' : '#560319', 
'dark sea green' : '#8FBC8F', 
'dark sienna' : '#3C1414', 
'dark slate blue' : '#483D8B', 
'dark slate gray' : '#2F4F4F', 
'dark spring green' : '#177245', 
'dark tan' : '#918151', 
'dark tangerine' : '#FFA812', 
'dark taupe' : '#483C32', 
'dark terra cotta' : '#CC4E5C', 
'dark turquoise' : '#00CED1', 
'dark violet' : '#9400D3', 
'dartmouth green' : '#00693E', 
'davys grey' : '#555555', 
'debian red' : '#D70A53', 
'deep carmine' : '#A9203E', 
'deep carmine pink' : '#EF3038', 
'deep carrot orange' : '#E9692C', 
'deep cerise' : '#DA3287', 
'deep champagne' : '#FAD6A5', 
'deep chestnut' : '#B94E48', 
'deep coffee' : '#704241', 
'deep fuchsia' : '#C154C1', 
'deep jungle green' : '#004B49', 
'deep lilac' : '#9955BB', 
'deep magenta' : '#CC00CC', 
'deep peach' : '#FFCBA4', 
'deep pink' : '#FF1493', 
'deep saffron' : '#FF9933', 
'deep sky blue' : '#00BFFF', 
'denim' : '#1560BD', 
'desert' : '#C19A6B', 
'desert sand' : '#EDC9AF', 
'dim gray' : '#696969', 
'dodger blue' : '#1E90FF', 
'dogwood rose' : '#D71868', 
'dollar bill' : '#85BB65', 
'drab' : '#967117', 
'duke blue' : '#00009C', 
'earth yellow' : '#E1A95F', 
'ecru' : '#C2B280', 
'eggplant' : '#614051', 
'eggshell' : '#F0EAD6', 
'egyptian blue' : '#1034A6', 
'electric blue' : '#7DF9FF', 
'electric crimson' : '#FF003F', 
'electric cyan' : '#00FFFF', 
'electric green' : '#00FF00', 
'electric indigo' : '#6F00FF', 
'electric lavender' : '#F4BBFF', 
'electric lime' : '#CCFF00', 
'electric purple' : '#BF00FF', 
'electric ultramarine' : '#3F00FF', 
'electric violet' : '#8F00FF', 
'electric yellow' : '#FFFF00', 
'emerald' : '#50C878', 
'eton blue' : '#96C8A2', 
'fallow' : '#C19A6B', 
'falu red' : '#801818', 
'fandango' : '#B53389', 
'fashion fuchsia' : '#F400A1', 
'fawn' : '#E5AA70', 
'feldgrau' : '#4D5D53', 
'fern green' : '#4F7942', 
'ferrari red' : '#FF2800', 
'field drab' : '#6C541E', 
'firebrick' : '#B22222', 
'fire engine red' : '#CE2029', 
'flame' : '#E25822', 
'flamingo pink' : '#FC8EAC', 
'flavescent' : '#F7E98E', 
'flax' : '#EEDC82', 
'floral white' : '#FFFAF0', 
'fluorescent orange' : '#FFBF00', 
'fluorescent pink' : '#FF1493', 
'fluorescent yellow' : '#CCFF00', 
'folly' : '#FF004F', 
'forest green (traditional)' : '#014421', 
'forest green (web)' : '#228B22', 
'french beige' : '#A67B5B', 
'french blue' : '#0072BB', 
'french lilac' : '#86608E', 
'french rose' : '#F64A8A', 
'fuchsia' : '#FF00FF', 
'fuchsia pink' : '#FF77FF', 
'fulvous' : '#E48400', 
'fuzzy wuzzy' : '#CC6666', 
'gainsboro' : '#DCDCDC', 
'gamboge' : '#E49B0F', 
'ghost white' : '#F8F8FF', 
'ginger' : '#B06500', 
'glaucous' : '#6082B6', 
'glitter' : '#E6E8FA', 
'gold (metallic)' : '#D4AF37', 
'gold (web) (golden)' : '#FFD700', 
'golden brown' : '#996515', 
'golden poppy' : '#FCC200', 
'golden yellow' : '#FFDF00', 
'goldenrod' : '#DAA520', 
'granny smith apple' : '#A8E4A0', 
'gray' : '#808080', 
'gray (web)' : '#7F7F7F', 
'gray (x11)' : '#BEBEBE', 
'gray-asparagus' : '#465945', 
'green (x11)' : '#00FF00', 
'green (web)' : '#008000', 
'green (munsell)' : '#00A877', 
'green (ncs)' : '#009F6B', 
'green (pigment)' : '#00A550', 
'green (ryb)' : '#66B032', 
'green-yellow' : '#ADFF2F', 
'grullo' : '#A99A86', 
'guppie green' : '#00FF7F', 
'halaya ube' : '#663854', 
'han blue' : '#446CCF', 
'han purple' : '#5218FA', 
'hansa yellow' : '#E9D66B', 
'harlequin' : '#3FFF00', 
'harvard crimson' : '#C90016', 
'harvest gold' : '#DA9100', 
'heart gold' : '#808000', 
'heliotrope' : '#DF73FF', 
'hollywood cerise' : '#F400A1', 
'honeydew' : '#F0FFF0', 
'hookers green' : '#007000', 
'hot magenta' : '#FF1DCE', 
'hot pink' : '#FF69B4', 
'hunter green' : '#355E3B', 
'iceberg' : '#71A6D2', 
'icterine' : '#FCF75E', 
'inchworm' : '#B2EC5D', 
'india green' : '#138808', 
'indian red' : '#CD5C5C', 
'indian yellow' : '#E3A857', 
'indigo (dye)' : '#00416A', 
'indigo (web)' : '#4B0082', 
'international klein blue' : '#002FA7', 
'international orange' : '#FF4F00', 
'iris' : '#5A4FCF', 
'isabelline' : '#F4F0EC', 
'islamic green' : '#009000', 
'ivory' : '#FFFFF0', 
'jade' : '#00A86B', 
'jasper' : '#D73B3E', 
'jasmine' : '#F8DE7E', 
'jazzberry jam' : '#A50B5E', 
'jonquil' : '#FADA5E', 
'june bud' : '#BDDA57', 
'jungle green' : '#29AB87', 
'kelly green' : '#4CBB17', 
'khaki (web)' : '#C3B091', 
'khaki (x11)' : '#F0E68C', 
'ku crimson' : '#E8000D', 
'la salle green' : '#087830', 
'languid lavender' : '#D6CADD', 
'lapis lazuli' : '#26619C', 
'laser lemon' : '#FEFE22', 
'lava' : '#CF1020', 
'lavender (floral)' : '#B57EDC', 
'lavender (web)' : '#E6E6FA', 
'lavender blue' : '#CCCCFF', 
'lavender blush' : '#FFF0F5', 
'lavender gray' : '#C4C3D0', 
'lavender indigo' : '#9457EB', 
'lavender magenta' : '#EE82EE', 
'lavender mist' : '#E6E6FA', 
'lavender pink' : '#FBAED2', 
'lavender purple' : '#967BB6', 
'lavender rose' : '#FBA0E3', 
'lawn green' : '#7CFC00', 
'lemon' : '#FFF700', 
'lemon chiffon' : '#FFFACD', 
'light apricot' : '#FDD5B1', 
'light blue' : '#ADD8E6', 
'light brown' : '#B5651D', 
'light carmine pink' : '#E66771', 
'light coral' : '#F08080', 
'light cornflower blue' : '#93CCEA', 
'light crimson' : '#F56991', 
'light cyan' : '#E0FFFF', 
'light fuchsia pink' : '#F984EF', 
'light goldenrod yellow' : '#FAFAD2', 
'light gray' : '#D3D3D3', 
'light green' : '#90EE90', 
'light khaki' : '#F0E68C', 
'light mauve' : '#DCD0FF', 
'light pastel purple' : '#B19CD9', 
'light pink' : '#FFB6C1', 
'light salmon' : '#FFA07A', 
'light salmon pink' : '#FF9999', 
'light sea green' : '#20B2AA', 
'light sky blue' : '#87CEFA', 
'light slate gray' : '#778899', 
'light taupe' : '#B38B6D', 
'light thulian pink' : '#E68FAC', 
'light yellow' : '#FFFFED', 
'lilac' : '#C8A2C8', 
'lime (color wheel)' : '#BFFF00', 
'lime (web)' : '#00FF00', 
'lime green' : '#32CD32', 
'lincoln green' : '#195905', 
'linen' : '#FAF0E6', 
'liver' : '#534B4F', 
'lust' : '#E62020', 
'magenta' : '#FF00FF', 
'magenta (dye)' : '#CA1F7B', 
'magenta (process)' : '#FF0090', 
'magic mint' : '#AAF0D1', 
'magnolia' : '#F8F4FF', 
'mahogany' : '#C04000', 
'maize' : '#FBEC5D', 
'majorelle blue' : '#6050DC', 
'malachite' : '#0BDA51', 
'manatee' : '#979AAA', 
'mango tango' : '#FF8243', 
'maroon (web)' : '#800000', 
'maroon (x11)' : '#B03060', 
'mauve' : '#E0B0FF', 
'mauve taupe' : '#915F6D', 
'mauvelous' : '#EF98AA', 
'maya blue' : '#73C2FB', 
'meat brown' : '#E5B73B', 
'medium aquamarine' : '#66DDAA', 
'medium blue' : '#0000CD', 
'medium candy apple red' : '#E2062C', 
'medium carmine' : '#AF4035', 
'medium champagne' : '#F3E5AB', 
'medium electric blue' : '#035096', 
'medium jungle green' : '#1C352D', 
'medium lavender magenta' : '#DDA0DD', 
'medium orchid' : '#BA55D3', 
'medium persian blue' : '#0067A5', 
'medium purple' : '#9370DB', 
'medium red-violet' : '#BB3385', 
'medium sea green' : '#3CB371', 
'medium slate blue' : '#7B68EE', 
'medium spring bud' : '#C9DC87', 
'medium spring green' : '#00FA9A', 
'medium taupe' : '#674C47', 
'medium teal blue' : '#0054B4', 
'medium turquoise' : '#48D1CC', 
'medium violet-red' : '#C71585', 
'melon' : '#FDBCB4', 
'midnight blue' : '#191970', 
'midnight green (eagle green)' : '#004953', 
'mikado yellow' : '#FFC40C', 
'mint' : '#3EB489', 
'mint cream' : '#F5FFFA', 
'mint green' : '#98FF98', 
'misty rose' : '#FFE4E1', 
'moccasin' : '#FAEBD7', 
'mode beige' : '#967117', 
'moonstone blue' : '#73A9C2', 
'mordant red 19' : '#AE0C00', 
'moss green' : '#ADDFAD', 
'mountain meadow' : '#30BA8F', 
'mountbatten pink' : '#997A8D', 
'mulberry' : '#C54B8C', 
'mustard' : '#FFDB58', 
'myrtle' : '#21421E', 
'msu green' : '#18453B', 
'nadeshiko pink' : '#F6ADC6', 
'napier green' : '#2A8000', 
'naples yellow' : '#FADA5E', 
'navajo white' : '#FFDEAD', 
'navy blue' : '#000080', 
'neon carrot' : '#FFA343', 
'neon fuchsia' : '#FE59C2', 
'neon green' : '#39FF14', 
'non-photo blue' : '#A4DDED', 
'north texas green' : '#059033', 
'ocean boat blue' : '#0077BE', 
'ochre' : '#CC7722', 
'office green' : '#008000', 
'old gold' : '#CFB53B', 
'old lace' : '#FDF5E6', 
'old lavender' : '#796878', 
'old mauve' : '#673147', 
'old rose' : '#C08081', 
'olive' : '#808000', 
'olive drab (web)' : '#6B8E23', 
'olive drab' : '#3C341F', 
'olivine' : '#9AB973', 
'onyx' : '#0F0F0F', 
'opera mauve' : '#B784A7', 
'orange (color wheel)' : '#FF7F00', 
'orange (ryb)' : '#FB9902', 
'orange (web)' : '#FFA500', 
'orange peel' : '#FF9F00', 
'orange-red' : '#FF4500', 
'orchid' : '#DA70D6', 
'otter brown' : '#654321', 
'outer space' : '#414A4C', 
'outrageous orange' : '#FF6E4A', 
'oxford blue' : '#002147', 
'ou crimson red' : '#990000', 
'pakistan green' : '#006600', 
'palatinate blue' : '#273BE2', 
'palatinate purple' : '#682860', 
'pale aqua' : '#BCD4E6', 
'pale blue' : '#AFEEEE', 
'pale brown' : '#987654', 
'pale carmine' : '#AF4035', 
'pale cerulean' : '#9BC4E2', 
'pale chestnut' : '#DDADAF', 
'pale copper' : '#DA8A67', 
'pale cornflower blue' : '#ABCDEF', 
'pale gold' : '#E6BE8A', 
'pale goldenrod' : '#EEE8AA', 
'pale green' : '#98FB98', 
'pale magenta' : '#F984E5', 
'pale pink' : '#FADADD', 
'pale plum' : '#DDA0DD', 
'pale red-violet' : '#DB7093', 
'pale robin egg blue' : '#96DED1', 
'pale silver' : '#C9C0BB', 
'pale spring bud' : '#ECEBBD', 
'pale taupe' : '#BC987E', 
'pale violet-red' : '#DB7093', 
'pansy purple' : '#78184A', 
'papaya whip' : '#FFEFD5', 
'paris green' : '#50C878', 
'pastel blue' : '#AEC6CF', 
'pastel brown' : '#836953', 
'pastel gray' : '#CFCFC4', 
'pastel green' : '#77DD77', 
'pastel magenta' : '#F49AC2', 
'pastel orange' : '#FFB347', 
'pastel pink' : '#FFD1DC', 
'pastel purple' : '#B39EB5', 
'pastel red' : '#FF6961', 
'pastel violet' : '#CB99C9', 
'pastel yellow' : '#FDFD96', 
'patriarch' : '#800080', 
'paynes grey' : '#40404F', 
'peach' : '#FFE5B4', 
'peach-orange' : '#FFCC99', 
'peach puff' : '#FFDAB9', 
'peach-yellow' : '#FADFAD', 
'pear' : '#D1E231', 
'pearl' : '#F0EAD6', 
'pearl aqua' : '#88D8C0', 
'peridot' : '#E6E200', 
'periwinkle' : '#CCCCFF', 
'persian blue' : '#1C39BB', 
'persian green' : '#00A693', 
'persian indigo' : '#32127A', 
'persian orange' : '#D99058', 
'persian pink' : '#F77FBE', 
'persian plum' : '#701C1C', 
'persian red' : '#CC3333', 
'persian rose' : '#FE28A2', 
'persimmon' : '#EC5800', 
'phlox' : '#DF00FF', 
'phthalo blue' : '#000F89', 
'phthalo green' : '#123524', 
'piggy pink' : '#FDDDE6', 
'pine green' : '#01796F', 
'pink' : '#FFC0CB', 
'pink-orange' : '#FF9966', 
'pink pearl' : '#E7ACCF', 
'pink sherbet' : '#F78FA7', 
'pistachio' : '#93C572', 
'platinum' : '#E5E4E2', 
'plum (traditional)' : '#8E4585', 
'plum (web)' : '#DDA0DD', 
'portland orange' : '#FF5A36', 
'powder blue (web)' : '#B0E0E6', 
'princeton orange' : '#FF8F00', 
'prune' : '#701C1C', 
'prussian blue' : '#003153', 
'psychedelic purple' : '#DF00FF', 
'puce' : '#CC8899', 
'pumpkin' : '#FF7518', 
'purple (web)' : '#800080', 
'purple (munsell)' : '#9F00C5', 
'purple (x11)' : '#A020F0', 
'purple heart' : '#69359C', 
'purple mountain majesty' : '#9678B6', 
'purple pizzazz' : '#FE4EDA', 
'purple taupe' : '#50404D', 
'quartz' : '#51484F', 
'radical red' : '#FF355E', 
'raspberry' : '#E30B5D', 
'raspberry glace' : '#915F6D', 
'raspberry pink' : '#E25098', 
'raspberry rose' : '#B3446C', 
'raw umber' : '#826644', 
'razzle dazzle rose' : '#FF33CC', 
'razzmatazz' : '#E3256B', 
'red' : '#FF0000', 
'red (munsell)' : '#F2003C', 
'red (ncs)' : '#C40233', 
'red (pigment)' : '#ED1C24', 
'red (ryb)' : '#FE2712', 
'red-brown' : '#A52A2A', 
'red-violet' : '#C71585', 
'redwood' : '#AB4E52', 
'regalia' : '#522D80', 
'rich black' : '#004040', 
'rich brilliant lavender' : '#F1A7FE', 
'rich carmine' : '#D70040', 
'rich electric blue' : '#0892D0', 
'rich lavender' : '#A76BCF', 
'rich lilac' : '#B666D2', 
'rich maroon' : '#B03060', 
'rifle green' : '#414833', 
'robin egg blue' : '#00CCCC', 
'rose' : '#FF007F', 
'rose bonbon' : '#F9429E', 
'rose ebony' : '#674846', 
'rose gold' : '#B76E79', 
'rose madder' : '#E32636', 
'rose pink' : '#FF66CC', 
'rose quartz' : '#AA98A9', 
'rose taupe' : '#905D5D', 
'rose vale' : '#AB4E52', 
'rosewood' : '#65000B', 
'rosso corsa' : '#D40000', 
'rosy brown' : '#BC8F8F', 
'royal azure' : '#0038A8', 
'royal blue (traditional)' : '#002366', 
'royal blue (web)' : '#4169E1', 
'royal fuchsia' : '#CA2C92', 
'royal purple' : '#7851A9', 
'ruby' : '#E0115F', 
'ruddy' : '#FF0028', 
'ruddy brown' : '#BB6528', 
'ruddy pink' : '#E18E96', 
'rufous' : '#A81C07', 
'russet' : '#80461B', 
'rust' : '#B7410E', 
'sacramento state green' : '#00563F', 
'saddle brown' : '#8B4513', 
'safety orange (blaze orange)' : '#FF6700', 
'saffron' : '#F4C430', 
'st. patricks blue' : '#23297A', 
'salmon' : '#FF8C69', 
'salmon pink' : '#FF91A4', 
'sand' : '#C2B280', 
'sand dune' : '#967117', 
'sandstorm' : '#ECD540', 
'sandy brown' : '#F4A460', 
'sandy taupe' : '#967117', 
'sangria' : '#92000A', 
'sap green' : '#507D2A', 
'sapphire' : '#082567', 
'satin sheen gold' : '#CBA135', 
'scarlet' : '#FF2400', 
'school bus yellow' : '#FFD800', 
'screamin green' : '#76FF7A', 
'sea green' : '#2E8B57', 
'seal brown' : '#321414', 
'seashell' : '#FFF5EE', 
'selective yellow' : '#FFBA00', 
'sepia' : '#704214', 
'shadow' : '#8A795D', 
'shamrock green' : '#009E60', 
'shocking pink' : '#FC0FC0', 
'sienna' : '#882D17', 
'silver' : '#C0C0C0', 
'sinopia' : '#CB410B', 
'skobeloff' : '#007474', 
'sky blue' : '#87CEEB', 
'sky magenta' : '#CF71AF', 
'slate blue' : '#6A5ACD', 
'slate gray' : '#708090', 
'smalt (dark powder blue)' : '#003399', 
'smokey topaz' : '#933D41', 
'smoky black' : '#100C08', 
'snow' : '#FFFAFA', 
'spiro disco ball' : '#0FC0FC', 
'splashed white' : '#FEFDFF', 
'spring bud' : '#A7FC00', 
'spring green' : '#00FF7F', 
'steel blue' : '#4682B4', 
'stil de grain yellow' : '#FADA5E', 
'stizza' : '#990000', 
'straw' : '#E4D96F', 
'sunglow' : '#FFCC33', 
'sunset' : '#FAD6A5', 
'tan' : '#D2B48C', 
'tangelo' : '#F94D00', 
'tangerine' : '#F28500', 
'tangerine yellow' : '#FFCC00', 
'taupe' : '#483C32', 
'taupe gray' : '#8B8589', 
'tea green' : '#D0F0C0', 
'tea rose (orange)' : '#F88379', 
'tea rose (rose)' : '#F4C2C2', 
'teal' : '#008080', 
'teal blue' : '#367588', 
'teal green' : '#006D5B', 
'tenné (tawny)' : '#CD5700', 
'terra cotta' : '#E2725B', 
'thistle' : '#D8BFD8', 
'thulian pink' : '#DE6FA1', 
'tickle me pink' : '#FC89AC', 
'tiffany blue' : '#0ABAB5', 
'tigers eye' : '#E08D3C', 
'timberwolf' : '#DBD7D2', 
'titanium yellow' : '#EEE600', 
'tomato' : '#FF6347', 
'toolbox' : '#746CC0', 
'topaz' : '#FFC87C', 
'tractor red' : '#FD0E35', 
'trolley grey' : '#808080', 
'tropical rain forest' : '#00755E', 
'true blue' : '#0073CF', 
'tufts blue' : '#417DC1', 
'tumbleweed' : '#DEAA88', 
'turkish rose' : '#B57281', 
'turquoise' : '#30D5C8', 
'turquoise blue' : '#00FFEF', 
'turquoise green' : '#A0D6B4', 
'tuscan red' : '#66424D', 
'twilight lavender' : '#8A496B', 
'tyrian purple' : '#66023C', 
'ua blue' : '#0033AA', 
'ua red' : '#D9004C', 
'ube' : '#8878C3', 
'ucla blue' : '#536895', 
'ucla gold' : '#FFB300', 
'ufo green' : '#3CD070', 
'ultramarine' : '#120A8F', 
'ultramarine blue' : '#4166F5', 
'ultra pink' : '#FF6FFF', 
'umber' : '#635147', 
'united nations blue' : '#5B92E5', 
'university of california gold' : '#B78727', 
'unmellow yellow' : '#FFFF66', 
'up forest green' : '#014421', 
'up maroon' : '#7B1113', 
'upsdell red' : '#AE2029', 
'urobilin' : '#E1AD21', 
'usc cardinal' : '#990000', 
'usc gold' : '#FFCC00', 
'utah crimson' : '#D3003F', 
'vanilla' : '#F3E5AB', 
'vegas gold' : '#C5B358', 
'venetian red' : '#C80815', 
'verdigris' : '#43B3AE', 
'vermilion' : '#E34234', 
'veronica' : '#A020F0', 
'violet' : '#8F00FF', 
'violet (color wheel)' : '#7F00FF', 
'violet (ryb)' : '#8601AF', 
'violet (web)' : '#EE82EE', 
'viridian' : '#40826D', 
'vivid auburn' : '#922724', 
'vivid burgundy' : '#9F1D35', 
'vivid cerise' : '#DA1D81', 
'vivid tangerine' : '#FFA089', 
'vivid violet' : '#9F00FF', 
'warm black' : '#004242', 
'wenge' : '#645452', 
'wheat' : '#F5DEB3', 
'white' : '#FFFFFF', 
'white smoke' : '#F5F5F5', 
'wild blue yonder' : '#A2ADD0', 
'wild strawberry' : '#FF43A4', 
'wild watermelon' : '#FC6C85', 
'wine' : '#722F37', 
'wisteria' : '#C9A0DC', 
'xanadu' : '#738678', 
'yale blue' : '#0F4D92', 
'yellow' : '#FFFF00', 
'yellow (munsell)' : '#EFCC00', 
'yellow (ncs)' : '#FFD300', 
'yellow (process)' : '#FFEF00', 
'yellow (ryb)' : '#FEFE33', 
'yellow-green' : '#9ACD32', 
'yellow orange' : '#FFEF02', 
'zaffre' : '#0014A8', 
'zinnwaldite brown' : '#2C1608'
}

class ConfigurationManager:
	_parsedDom = None
	_stylingElement = None
	
	def __init__(self, xmlPath):
		try:
			xmlReader = open(xmlPath)
		except IOError:
			print('No such file or directory')
			raise IOError('Incorrect configuration path provided')
			
		try:
			self._parsedDom = parse(xmlReader)
		except (TypeError, AttributeError):
			print('Error processing the configuration')
			xmlReader.close()
			
		xmlReader.close()
	
	# returns object of type ComponentStyle or None if a component with the specified id does not exist 
	# in the current configuration
	def InitComponentStyle(self, componentId):
		if self._parsedDom.documentElement.nodeName != 'configuration':
			raise TypeError('Incorrect root node: pygame-ui config requires configuration as its root element')
		if self._stylingElement == None:
			self._stylingElement = self._parsedDom.documentElement.getElementsByTagName('styling')[0]
		if self._stylingElement == None:
			raise TypeError('Component node does not exist in the current configuration')
		
		for child in self._stylingElement.childNodes:
			if child.nodeName == 'component':
				if child.getAttribute('id') == componentId:
					return ComponentStyle(child)
		else:
			return None
			
	
			
	def FindAllComponents(self):
		if self._parsedDom.documentElement.nodeName != 'configuration':
			raise TypeError('Incorrect root node: pygame-ui config requires configuration as its root element')
		if self._stylingElement == None:
			self._stylingElement = self._parsedDom.documentElement.getElementsByTagName('styling')[0]
		if self._stylingElement == None:
			raise TypeError('Component node does not exist in the current configuration')
		
		componentList = []
		for child in self._stylingElement.childNodes:
			if child.nodeName == 'component':
				componentList.append((child.getAttribute('id'), child.getAttribute('type'), ComponentStyle(child)))
				
		return componentList

class ComponentStyle:
	_initialized = False
	_top = 0
	_left = 0
	_width = 0
	_widthUnit = 'px'
	_height = 0
	_heightUnit = 'px'
	_backgroundImage = None
	_backgroundColor = None
	_color = None
	_fontSize = 0
	_fontFamily = None
	_textAlign = 'left'
	_verticalAlign = 'top'
	_visibility = 'visible'
	_xmlNode = None
	
	def __init__(self, componentNode = None):
		if componentNode != None:
			self._xmlNode = componentNode
		else:
			self._initialized = True
		
	def __str__(self):
		return('{\n top: {0};\n left: {1};\n width: {2}{3};\n height: {4}{5};\n background-image: url({6});\n }\n', self.top, self.left, self.width, self.width_unit, self.height, self.height_unit, self.background_image)
		
	# ========================= Properties =========================
	
	@property
	def dimensions(self):
		if not self._initialized:
			self.InitStyles()
		return (self._width, self._height)
		
	@dimensions.setter
	def dimensions(self, value):
		self._width, self._height = value
		
	@property
	def width(self):
		if not self._initialized:
			self.InitStyles()
			
		return self._width
		
	@width.setter
	def width(self, value):
		self._width = value
		
	@property
	def width_unit(self):
		if not self._initialized:
			self.InitStyles()
			
		return self._widthUnit
	
	@property
	def height(self):
		if not self._initialized:
			self.InitStyles()
			
		return self._height
		
	@height.setter
	def height(self, value):
		self._height = value
		
	@property
	def height_unit(self):
		if not self._initialized:
			self.InitStyles()
			
		return self._heightUnit
		
	@property
	def position(self):
		if not self._initialized:
			self.InitStyles()
		
		return (self._top, self._left)
		
	@position.setter
	def position(self, value):
		self._top, self._left = value
	
	@property
	def top(self):
		if not self._initialized:
			self.InitStyles()
		
		return self._top
		
	@top.setter
	def top(self, value):
		self._top = value
		
	@property
	def left(self):
		if not self._initialized:
			self.InitStyles()
		
		return self._left
		
	@left.setter
	def left(self, value):
		self._left = value
	
	@property
	def background_image(self):
		if not self._initialized:
			self.InitStyles()
		
		return self._backgroundImage
	
	@background_image.setter
	def background_image(self, value):
		self._backgroundImage = value
		
	@property
	def background_color(self):
		if not self._initialized:
			self.InitStyles()
			
		return self._backgroundColor
		
	@background_color.setter
	def background_color(self, value):
		self._backgroundColor = value
		
	@property
	def color(self):
		if not self._initialized:
			self.InitStyles()
			
		return self._color
		
	@color.setter
	def color(self, value):
		self._color = self.ParseColor(value);
		
	@property
	def font_size(self):
		if not self._initialized:
			self.InitStyles()
			
		return self._fontSize
		
	@font_size.setter
	def font_size(self, value):
		self._fontSize = value
		
	@property
	def font_family(self):
		if not self._initialized:
			self.InitStyles()
			
		return self._fontFamily
		
	@font_family.setter
	def font_family(self, value):
		self._fontFamily = value
	
	@property
	def text_align(self):
		if not self._initialized:
			self.InitStyles()
			
		return self._textAlign
		
	@text_align.setter
	def text_align(self, value):
		self._textAlign = value
		
	@property
	def vertical_align(self):
		if not self._initialized:
			self.InitStyles()
			
		return self._verticalAlign
	
	@vertical_align.setter
	def vertical_align(self, value):
		self._verticalAlign = value
		
	@property
	def visibility(self):
		if not self._initialized:
			self.InitStyles()
			
		return self._visibility
		
	@visibility.setter
	def visibility(self, value):
		self._visibility = value
			
	def InitStyles(self):
		if self._xmlNode == None:
			raise TypeError('Component configuration node not found')
		else:
			for child in self._xmlNode.childNodes:
				if child.nodeName == 'width':
					unit = child.getAttribute('unit')
					if unit != None:
						self._widthUnit = unit
					self._width = int(child.firstChild.data)
				elif child.nodeName == 'height':
					unit = child.getAttribute('unit')
					if unit != None:
						self._heightUnit = unit
					self._height = int(child.firstChild.data)
				elif child.nodeName == 'top':
					self._top = int(child.firstChild.data)
				elif child.nodeName == 'left':
					self._left = int(child.firstChild.data)
				elif child.nodeName == 'fontFamily':
					self._fontFamily = child.firstChild.data
				elif child.nodeName == 'fontSize':
					self._fontSize = child.firstChild.data
				elif child.nodeName == 'backgroundImage':
					self._backgroundImage = child.firstChild.data
				elif child.nodeName == 'backgroundColor':
					self._backgroundColor = self.ParseColor(child.firstChild.data)
				elif child.nodeName == 'color':
					self._color = self.ParseColor(child.firstChild.data)
				elif child.nodeName == 'textAlign':
					self._textAlign = child.firstChild.data
				elif child.nodeName == 'verticalAlign':
					self._verticalAlign = child.firstChild.data
				elif child.nodeName == 'visibility':
					self._visibility = child.firstChild.data
					
			self._initialized = True
					
	def ParseColor(self, color):
		# RGB color definition
		if color[0] == '#':
			color = color[1:]
			if len(color) == 6:
				return pygame.Color(int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16))
			elif len(color) == 3:
				return pygame.Color(int(color[0:1] * 2, 16), int(color[1:2] * 2, 16), int(color[2:3] * 2, 16))
			else:
				pass
				# parse color of type keyword e.g. Black, red, YELLOW, etc.
		else:
			return color
