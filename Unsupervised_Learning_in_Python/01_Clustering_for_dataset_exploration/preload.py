import numpy as np
import pandas as pd

points = np.array([[0.06544649, -0.76866376],
                   [-1.52901547, -0.42953079],
                   [1.70993371, 0.69885253],
                   [1.16779145, 1.01262638],
                   [-1.80110088, -0.31861296],
                   [-1.63567888, -0.02859535],
                   [1.21990375, 0.74643463],
                   [-0.26175155, -0.62492939],
                   [-1.61925804, -0.47983949],
                   [-1.84329582, -0.16694431],
                   [1.35999602, 0.94995827],
                   [0.42291856, -0.7349534],
                   [-1.68576139, 0.10686728],
                   [0.90629995, 1.09105162],
                   [-1.56478322, -0.84675394],
                   [-0.0257849, -1.18672539],
                   [0.83027324, 1.14504612],
                   [1.22450432, 1.35066759],
                   [-0.15394596, -0.71704301],
                   [0.86358809, 1.06824613],
                   [-1.43386366, -0.2381297],
                   [0.03844769, -0.74635022],
                   [-1.58567922, 0.08499354],
                   [0.6359888, -0.58477698],
                   [0.24417242, -0.53172465],
                   [-2.19680359, 0.49473677],
                   [1.0323503, -0.55688],
                   [-0.28858067, -0.39972528],
                   [0.20597008, -0.80171536],
                   [-1.2107308, -0.34924109],
                   [1.33423684, 0.7721489],
                   [1.19480152, 1.04788556],
                   [0.9917477, 0.89202008],
                   [-1.8356219, -0.04839732],
                   [0.08415721, -0.71564326],
                   [-1.48970175, -0.19299604],
                   [0.38782418, -0.82060119],
                   [-0.01448044, -0.9779841],
                   [-2.0521341, -0.02129125],
                   [0.10331194, -0.82162781],
                   [-0.44189315, -0.65710974],
                   [1.10390926, 1.02481182],
                   [-1.59227759, -0.17374038],
                   [-1.47344152, -0.02202853],
                   [-1.35514704, 0.22971067],
                   [0.0412337, -1.23776622],
                   [0.4761517, -1.13672124],
                   [1.04335676, 0.82345905],
                   [-0.07961882, -0.85677394],
                   [0.87065059, 1.08052841],
                   [1.40267313, 1.07525119],
                   [0.80111157, 1.28342825],
                   [-0.16527516, -1.23583804],
                   [-0.33779221, -0.59194323],
                   [0.80610749, -0.73752159],
                   [-1.43590032, -0.56384446],
                   [0.54868895, -0.95143829],
                   [0.46803131, -0.74973907],
                   [-1.5137129, -0.83914323],
                   [0.9138436, 1.51126532],
                   [-1.97233903, -0.41155375],
                   [0.5213406, -0.88654894],
                   [0.62759494, -1.18590477],
                   [0.94163014, 1.35399335],
                   [0.56994768, 1.07036606],
                   [-1.87663382, 0.14745773],
                   [0.90612186, 0.91084011],
                   [-1.37481454, 0.28428395],
                   [-1.80564029, -0.96710574],
                   [0.34307757, -0.79999275],
                   [0.70380566, 1.00025804],
                   [-1.68489862, -0.30564595],
                   [1.31473221, 0.98614978],
                   [0.26151216, -0.26069251],
                   [0.9193121, 0.82371485],
                   [-1.21795929, -0.20219674],
                   [-0.17722723, -1.02665245],
                   [0.64824862, -0.66822881],
                   [0.41206786, -0.28783784],
                   [1.01568202, 1.13481667],
                   [0.67900254, -0.91489502],
                   [-1.05182747, -0.01062376],
                   [0.61306599, 1.78210384],
                   [-1.50219748, -0.52308922],
                   [-1.72717293, -0.46173916],
                   [-1.60995631, -0.1821007],
                   [-1.09111021, -0.0781398],
                   [-0.01046978, -0.80913034],
                   [0.32782303, -0.80734754],
                   [1.22038503, 1.1959793],
                   [-1.33328681, -0.30001937],
                   [0.87959517, 1.11566491],
                   [-1.14829098, -0.30400762],
                   [-0.58019755, -1.19996018],
                   [-0.01161159, -0.78468854],
                   [0.17359724, -0.63398145],
                   [1.32738556, 0.67759969],
                   [-1.93467327, 0.30572472],
                   [-1.57761893, -0.27726365],
                   [0.47639, 1.21422648],
                   [-1.65237509, -0.6803981],
                   [-0.12609976, -1.04327457],
                   [-1.89607082, -0.70085502],
                   [0.57466899, 0.74878369],
                   [-0.16660312, -0.83110295],
                   [0.8013355, 1.22244435],
                   [1.18455426, 1.4346467],
                   [1.08864428, 0.64667112],
                   [-1.61158505, 0.22805725],
                   [-1.57512205, -0.09612576],
                   [0.0721357, -0.69640328],
                   [-1.40054298, 0.16390598],
                   [1.09607713, 1.16804691],
                   [-2.54346204, -0.23089822],
                   [-1.34544875, 0.25151126],
                   [-1.35478629, -0.19103317],
                   [0.18368113, -1.15827725],
                   [-1.31368677, -0.376357],
                   [0.09990129, 1.22500491],
                   [1.17225574, 1.30835143],
                   [0.0865397, -0.79714371],
                   [-0.21053923, -1.13421511],
                   [0.26496024, -0.94760742],
                   [-0.2557591, -1.06266022],
                   [-0.26039757, -0.74774225],
                   [-1.91787359, 0.16434571],
                   [0.93021139, 0.49436331],
                   [0.44770467, -0.72877918],
                   [-1.63802869, -0.58925528],
                   [-1.95712763, -0.10125137],
                   [0.9270337, 0.88251423],
                   [1.25660093, 0.60828073],
                   [-1.72818632, 0.08416887],
                   [0.3499788, -0.30490298],
                   [-1.51696082, -0.50913109],
                   [0.18763605, -0.55424924],
                   [0.89609809, 0.83551508],
                   [-1.54968857, -0.17114782],
                   [1.2157457, 1.23317728],
                   [0.20307745, -1.03784906],
                   [0.84589086, 1.03615273],
                   [0.53237919, 1.47362884],
                   [-0.05319044, -1.36150553],
                   [1.38819743, 1.11729915],
                   [1.00696304, 1.0367721],
                   [0.56681869, -1.09637176],
                   [0.86888296, 1.05248874],
                   [-1.16286609, -0.55875245],
                   [0.27717768, -0.83844015],
                   [0.16563267, -0.80306607],
                   [0.38263303, -0.42683241],
                   [1.14519807, 0.89659026],
                   [0.81455857, 0.67533667],
                   [-1.8603152, -0.09537561],
                   [0.965641, 0.90295579],
                   [-1.49897451, -0.33254044],
                   [-0.1335489, -0.80727582],
                   [0.12541527, -1.13354906],
                   [1.06062436, 1.28816358],
                   [-1.49154578, -0.2024641],
                   [1.16189032, 1.28819877],
                   [0.54282033, 0.75203524],
                   [0.89221065, 0.99211624],
                   [-1.49932011, -0.32430667],
                   [0.3166647, -1.34482915],
                   [0.13972469, -1.22097448],
                   [-1.5499724, -0.10782584],
                   [1.23846858, 1.37668804],
                   [1.25558954, 0.72026098],
                   [0.25558689, -1.28529763],
                   [0.45168933, -0.55952093],
                   [1.06202057, 1.03404604],
                   [0.67451908, -0.54970299],
                   [0.22759676, -1.02729468],
                   [-1.45835281, -0.04951074],
                   [0.23273501, -0.70849262],
                   [1.59679589, 1.11395076],
                   [0.80476105, 0.544627],
                   [1.15492521, 1.04352191],
                   [0.59632776, -1.19142897],
                   [0.02839068, -0.43829366],
                   [1.13451584, 0.5632633],
                   [0.21576204, -1.04445753],
                   [1.41048987, 1.02830719],
                   [1.12289302, 0.58029441],
                   [0.25200688, -0.82588436],
                   [-1.28566081, -0.07390909],
                   [1.52849815, 1.11822469],
                   [-0.23907858, -0.70541972],
                   [-0.25792784, -0.81825035],
                   [0.59367818, -0.45239915],
                   [0.07931909, -0.29233213],
                   [-1.27256815, 0.11630577],
                   [0.66930129, 1.00731481],
                   [0.34791546, -1.20822877],
                   [-2.11283993, -0.66897935],
                   [-1.6293824, -0.32718222],
                   [-1.53819139, -0.01501972],
                   [-0.11988545, -0.6036339],
                   [-1.54418956, -0.30389844],
                   [0.30026614, -0.77723173],
                   [0.00935449, -0.53888192],
                   [-1.33424393, -0.11560431],
                   [0.47504489, 0.78421384],
                   [0.59313264, 1.232239],
                   [0.41370369, -1.35205857],
                   [0.55840948, 0.78831053],
                   [0.49855018, -0.789949],
                   [0.35675809, -0.81038693],
                   [-1.86197825, -0.59071305],
                   [-1.61977671, -0.16076687],
                   [0.80779295, -0.73311294],
                   [1.62745775, 0.62787163],
                   [-1.56993593, -0.08467567],
                   [1.02558561, 0.89383302],
                   [0.24293461, -0.6088253],
                   [1.23130242, 1.00262186],
                   [-1.9651013, -0.15886289],
                   [0.42795032, -0.70384432],
                   [-1.58306818, -0.19431923],
                   [-1.57195922, 0.01413469],
                   [-0.98145373, 0.06132285],
                   [-1.48637844, -0.5746531],
                   [0.98745828, 0.69188053],
                   [1.28619721, 1.28128821],
                   [0.85850596, 0.95541481],
                   [0.19028286, -0.82112942],
                   [0.26561046, -0.04255239],
                   [-1.61897897, 0.00862372],
                   [0.24070183, -0.52664209],
                   [1.15220993, 0.43916694],
                   [-1.21967812, -0.2580313],
                   [0.33412533, -0.86117761],
                   [0.17131003, -0.75638965],
                   [-1.19828397, -0.73744665],
                   [-0.12245932, -0.45648879],
                   [1.51200698, 0.88825741],
                   [1.10338866, 0.92347479],
                   [1.30972095, 0.59066989],
                   [0.19964876, 1.14855889],
                   [0.81460515, 0.84538972],
                   [-1.6422739, -0.42296206],
                   [0.01224351, -0.21247816],
                   [0.33709102, -0.74618065],
                   [0.47301054, 0.72712075],
                   [0.34706626, 1.23033757],
                   [-0.00393279, -0.97209694],
                   [-1.64303119, 0.05276337],
                   [1.44649625, 1.14217033],
                   [-1.93030087, -0.40026146],
                   [-2.37296135, -0.72633645],
                   [0.45860122, -1.06048953],
                   [0.4896361, -1.18928313],
                   [-1.02335902, -0.17520578],
                   [-1.32761107, -0.93963549],
                   [-1.50987909, -0.09473658],
                   [0.02723057, -0.79870549],
                   [1.0169412, 1.26461701],
                   [0.47733527, -0.9898471],
                   [-1.27784224, -0.547416],
                   [0.49898802, -0.6237259],
                   [1.06004731, 0.86870008],
                   [1.00207501, 1.38293512],
                   [1.31161394, 0.62833956],
                   [1.13428443, 1.18346542],
                   [1.27671346, 0.96632878],
                   [-0.63342885, -0.97768251],
                   [0.12698779, -0.93142317],
                   [-1.34510812, -0.23754226],
                   [-0.53162278, -1.25153594],
                   [0.21959934, -0.90269938],
                   [-1.78997479, -0.12115748],
                   [1.23197473, -0.07453764],
                   [1.4163536, 1.21551752],
                   [-1.90280976, -0.1638976],
                   [-0.22440081, -0.75454248],
                   [0.59559412, 0.92414553],
                   [1.21930773, 1.08175284],
                   [-1.99427535, -0.37587799],
                   [-1.27818474, -0.52454551],
                   [0.62352689, -1.01430108],
                   [0.14024251, -0.428266],
                   [-0.16145713, -1.16359731],
                   [-1.74795865, -0.06033101],
                   [-1.16659791, 0.0902393],
                   [0.41110408, -0.8084249],
                   [1.14757168, 0.77804528],
                   [-1.65590748, -0.40105446],
                   [-1.15306865, 0.00858699],
                   [0.60892121, 0.68974833],
                   [-0.08434138, -0.97615256],
                   [0.19170053, -0.42331438],
                   [0.29663162, -1.13357399],
                   [-1.36893628, -0.25052124],
                   [-0.08037807, -0.56784155],
                   [0.35695011, -1.15064408],
                   [0.02482179, -0.63594828],
                   [-1.49075558, -0.2482507],
                   [-1.408588, 0.25635431],
                   [-1.98274626, -0.54584475]])

new_points = np.array([[0.40023333, -1.26544471],
                       [0.80323037, 1.28260167],
                       [-1.39507552, 0.05572929],
                       [-0.34119268, -1.07661994],
                       [1.54781747, 1.40250049],
                       [0.24503202, -0.48344233],
                       [1.20706886, 0.88875261],
                       [1.25132628, 1.15555395],
                       [1.81004415, 0.96553073],
                       [-1.66963401, -0.30810351],
                       [-0.07174821, -0.9379397],
                       [0.68263193, 1.1025816],
                       [1.09039598, 1.43899529],
                       [-1.67645414, -0.50455705],
                       [-1.84447804, 0.04525395],
                       [1.24234851, 1.02088661],
                       [-1.86147041, 0.00638646],
                       [-1.46044943, 0.15325238],
                       [0.49898182, 0.89800606],
                       [0.98396224, 1.04369375],
                       [-1.83136742, -0.16363284],
                       [1.30622617, 1.07658717],
                       [0.35342033, -0.75132022],
                       [1.1395797, 1.5450386],
                       [0.29399569, -1.26135005],
                       [-1.14558225, -0.03787096],
                       [1.18716105, 0.60024066],
                       [-2.23211946, 0.23047509],
                       [-1.2832043, -0.39331457],
                       [0.4942967, -0.88397201],
                       [0.06318349, -0.91195223],
                       [0.93575954, 0.86682068],
                       [1.58014721, 1.03788392],
                       [1.0630496, 1.02706082],
                       [-1.39732536, -0.50516225],
                       [-0.10993524, -0.90811362],
                       [1.17346758, 0.94750109],
                       [0.92008451, 1.45767672],
                       [0.58265896, -0.90008683],
                       [0.95277233, 0.89904239],
                       [-1.37266956, -0.03178782],
                       [0.02127068, -0.70761419],
                       [0.32704905, -0.55599811],
                       [-1.71590267, 0.21522227],
                       [0.51251621, -0.76012825],
                       [1.13023469, 0.72245112],
                       [-1.4307431, -0.34278751],
                       [-1.82724625, 0.11765777],
                       [1.4180135, 1.1145508],
                       [1.26897304, 1.41925971],
                       [0.80407649, 1.63988557],
                       [0.83456775, 1.09956689],
                       [-1.24714732, -0.22352232],
                       [-1.29422537, 0.081877],
                       [-0.22737832, -0.41333139],
                       [0.21883039, -0.46818312],
                       [-1.22593414, 0.25559915],
                       [-1.31294033, -0.42889207],
                       [-1.33532382, 0.65205378],
                       [-0.30110023, -1.25156451],
                       [0.20277836, -0.90527744],
                       [1.01357784, 1.12378981],
                       [0.81832439, 0.86084126],
                       [1.26181556, 1.46613744],
                       [0.46486772, -0.79721246],
                       [0.3609089, 0.84410672],
                       [-2.1509831, -0.36958394],
                       [1.05005281, 0.87418136],
                       [0.10658007, -0.74926815],
                       [-1.73945723, 0.25218358],
                       [-0.11201769, -0.65246979],
                       [0.51661895, -0.64126758],
                       [0.32662179, -0.88060801],
                       [1.09017759, 1.10952558],
                       [0.36445958, -0.69421562],
                       [-1.90779318, 0.18738367],
                       [-1.95601829, 0.13995913],
                       [0.3185417, -0.4052717],
                       [0.7365127, 1.76416255],
                       [-1.44175162, -0.05723204],
                       [0.32175717, -0.53428382],
                       [-1.37317305, 0.04644846],
                       [0.06872259, -1.10522944],
                       [0.95931422, 0.65231621],
                       [-1.62641919, -0.56242328],
                       [1.06788305, 0.72926048],
                       [-1.79643547, -0.98830742],
                       [-0.09886284, -0.06811981],
                       [-0.1051357, 1.17022143],
                       [0.8799647, 1.25340317],
                       [0.98075341, 1.15486539],
                       [-0.0833225, -0.92484437],
                       [0.84875967, 1.09397425],
                       [1.32941649, 1.13734563],
                       [0.32378807, -0.74973245],
                       [-1.5261097, -0.24901693],
                       [-1.48598116, -0.26882861],
                       [-1.80479553, 0.1870527],
                       [-2.01907347, -0.44951165],
                       [0.2872024, -0.65548741],
                       [0.8222951, 1.38443234],
                       [-0.0356997, -0.80182581],
                       [-1.6695544, -0.1382585],
                       [-1.78226821, 0.29335303],
                       [0.72583714, -0.62337402],
                       [0.38843259, -0.7612835],
                       [1.49002783, 0.79567867],
                       [0.00065542, -0.7405807],
                       [-1.34533116, -0.47562994],
                       [-0.80384511, -0.30994301],
                       [-0.2490413, -1.00662418],
                       [-1.41095118, -0.07067441],
                       [-1.75119594, -0.30049134],
                       [-1.27942724, 0.1737746],
                       [0.33502818, 0.62476115],
                       [1.16819649, 1.18902251],
                       [0.71521046, 0.92607742],
                       [1.30057278, 0.91634956],
                       [-1.21697008, 0.11003948],
                       [-1.70707935, -0.05996595],
                       [1.20730655, 1.05480463],
                       [0.18689601, -0.95804723],
                       [0.80346347, 0.38613314],
                       [-1.7348679, -0.14983191],
                       [1.31261499, 1.11802982],
                       [0.40499315, -0.51090035],
                       [-1.93267968, 0.22076469],
                       [0.6560048, 0.96188716],
                       [-1.40588215, 0.1171344],
                       [-1.74306264, -0.0747474],
                       [0.54374541, 1.47209224],
                       [-1.97331669, -0.22712449],
                       [1.53901171, 1.36049081],
                       [-1.48323452, -0.49030206],
                       [0.38674848, -1.261734],
                       [1.17015716, 1.18549415],
                       [-0.08053817, -0.32192363],
                       [-0.06822732, -0.85282589],
                       [0.71350003, 1.2786852],
                       [-1.85014378, -0.50349056],
                       [0.06360853, -1.4125704],
                       [1.52966062, 0.96605657],
                       [0.16216571, -1.37374843],
                       [-0.3234745, -0.70662027],
                       [-1.51768993, 0.1876583],
                       [0.88889591, 0.76223716],
                       [0.48316403, 0.88193187],
                       [-0.05529978, -0.71130502],
                       [-1.57966441, -0.62922031],
                       [0.05513086, -0.84720676],
                       [-2.06001582, 0.05876978],
                       [1.11810855, 1.30254175],
                       [0.48701616, -0.99014394],
                       [-1.65518042, -0.16938638],
                       [-1.44349738, 0.19029924],
                       [-0.17007455, -0.82673602],
                       [-1.82433979, -0.30781463],
                       [1.03093485, 1.26457691],
                       [1.64431169, 1.27773115],
                       [-1.47617693, 0.02607839],
                       [1.00953067, 1.14270181],
                       [-1.45285636, -0.25521621],
                       [-1.74092917, -0.08344432],
                       [1.22038299, 1.28699961],
                       [0.9169254, 0.73207028],
                       [-0.00160754, -0.72637557],
                       [0.89384124, 0.84114664],
                       [0.63379196, 1.00915134],
                       [-1.47927075, -0.69978194],
                       [0.05447994, -1.0644197],
                       [-1.51935568, -0.48927693],
                       [0.28993903, -0.77314552],
                       [-0.00968154, -1.13302207],
                       [1.13474639, 0.97154174],
                       [0.53642141, -0.84790639],
                       [1.14759864, 0.6899152],
                       [0.5732919, 0.79080271],
                       [0.2123774, -0.60756981],
                       [0.52657955, -0.81593026],
                       [-2.01831641, 0.06786507],
                       [-0.23551262, -1.08205132],
                       [0.15927478, -0.60071726],
                       [0.22812036, -1.16003549],
                       [-1.53658378, 0.08407988],
                       [1.13954609, 0.631782],
                       [1.01119255, 1.04360805],
                       [-0.14203987, -0.48123034],
                       [-2.23120182, 0.08491629],
                       [0.12555481, -1.01794793],
                       [-1.72493509, -0.69442618],
                       [-1.6043463, 0.44555087],
                       [0.73715398, 0.92656074],
                       [0.67290527, 1.1336603],
                       [1.20066456, 0.72627309],
                       [0.07587472, -0.98337833],
                       [1.28783262, 1.18088601],
                       [1.0652193, 1.00714746],
                       [1.05871698, 1.12956519],
                       [-1.1264341, 0.16678774],
                       [-1.10157218, -0.36413781],
                       [0.23511822, -0.13976995],
                       [1.13853795, 1.01018519],
                       [0.53120565, -0.88199079],
                       [0.43308594, -0.76405904],
                       [-0.00448926, -1.30548411],
                       [-1.76348589, -0.49743074],
                       [1.36485681, 0.5834047],
                       [0.5669239, 1.51391963],
                       [1.35736826, 0.67091532],
                       [1.07173397, 0.61199088],
                       [1.00106915, 0.89381533],
                       [1.33091007, 0.87977388],
                       [-1.7960374, -0.0353884],
                       [-1.27222979, 0.40015664],
                       [0.8474806, 1.17032364],
                       [-1.50989129, -0.71231833],
                       [-1.24953576, -0.55785973],
                       [-1.27717973, -0.59935055],
                       [-1.81946743, 0.73705767],
                       [1.19949867, 1.56969386],
                       [-1.25543847, -0.23389283],
                       [-1.63052058, 0.16145586],
                       [1.10611305, 0.73969822],
                       [0.67019319, 0.870567],
                       [0.36967016, -0.69464531],
                       [-1.26362293, -0.69924928],
                       [-0.36668751, -1.3531026],
                       [0.24403215, -0.65947079],
                       [-1.27679142, -0.48545341],
                       [0.03774736, -0.69925161],
                       [-2.19148539, -0.4911995],
                       [-0.29327778, -0.58948821],
                       [-1.65737397, -0.29833779],
                       [0.73663886, 0.57803706],
                       [1.13709081, 1.30119754],
                       [-1.44146601, 0.03139347],
                       [0.59236071, 1.22545114],
                       [0.65171941, 0.49267489],
                       [0.59455914, 0.82563732],
                       [-1.87900722, -0.52189963],
                       [0.21522504, -1.28269851],
                       [0.49914597, -0.67026863],
                       [-1.82954176, -0.33926973],
                       [0.7927214, 1.33785606],
                       [0.95436337, 0.98039663],
                       [-1.35359846, 0.10397634],
                       [1.05595062, 0.80703193],
                       [-1.9431101, -0.11897696],
                       [-1.39604137, -0.31009598],
                       [1.28977624, 1.01753365],
                       [-1.59503139, -0.54057461],
                       [-1.41994046, -0.38103257],
                       [-0.02355698, -1.10133702],
                       [-1.26038568, -0.69327389],
                       [0.96021598, -0.81155369],
                       [0.55180331, -1.01793176],
                       [0.37018509, -1.06885468],
                       [0.82552921, 0.87700706],
                       [-1.87032595, 0.2875072],
                       [-1.56260769, -0.18919671],
                       [-1.26346548, -0.77472524],
                       [-0.06338004, -0.75940061],
                       [0.88529828, 0.88562052],
                       [-0.14332469, -1.16083678],
                       [-1.83908725, -0.32665552],
                       [0.27470923, -1.04546829],
                       [-1.45703573, -0.29184204],
                       [-1.59048842, 0.16606303],
                       [0.92554928, 0.74140641],
                       [0.19724547, -0.78070322],
                       [0.2884017, -0.83242555],
                       [0.72414162, -0.7991492],
                       [-1.62658639, -0.18000554],
                       [0.58448159, 1.1319564],
                       [1.02146732, 0.4596578],
                       [0.86505055, 0.95771489],
                       [0.39871777, -1.24273147],
                       [0.86223489, 1.10955561],
                       [-1.3599943, 0.02499427],
                       [-1.19178505, -0.03829463],
                       [1.29392424, 1.10320509],
                       [1.2567963, -0.77985758],
                       [0.09380403, -0.55324726],
                       [-1.73512175, -0.09762717],
                       [0.22315359, -0.94347435],
                       [0.4019891, -1.10963051],
                       [-1.42244158, 0.1819147],
                       [0.39247627, -0.87842628],
                       [1.25181875, 0.693615],
                       [0.01774813, -0.72030424],
                       [-1.87752521, -0.26387042],
                       [-1.58063602, -0.55045634],
                       [-1.59589493, -0.15393289],
                       [-1.0182977, 0.03885424],
                       [1.24819659, 0.6600418],
                       [-1.25551377, -0.0296172],
                       [-1.41864559, -0.35823018],
                       [0.52575833, 0.87050054],
                       [0.55559999, 1.18765072],
                       [0.02813444, -0.69911131]])

seeds = pd.read_csv('../data/seeds_dataset.txt', delim_whitespace=True, header=None)
seeds_samples = seeds.iloc[:, :-1]
seeds_varieties = seeds.iloc[:, -1].replace({1: 'Kama wheat', 2: 'Rosa wheat', 3: 'Canadian wheat'}).tolist()

fish_catch = pd.read_csv('../data/fishcatch.dat.txt', delim_whitespace=True, header=None).iloc[:, :-1].dropna()
fish_catch_samples = fish_catch.iloc[:, 2:]
fish_catch_species = fish_catch.iloc[:, 1].replace(
    {
        1: 'Bream',
        2: 'Whitewish',
        3: 'Roach',
        4: 'Bjoerknan',
        5: 'Smelt',
        6: 'Pike',
        7: 'Perch',
    }
).tolist()

stock = pd.read_csv('../data/stock_movements.csv', header=None)
stock_movements = stock.iloc[:, 1:].to_numpy()
stock_companies = stock.iloc[:, 0].to_list()