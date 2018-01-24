import jieba
import jieba.posseg
import jieba.analyse

print('=' * 40)
print('3. 关键词提取')
print('-' * 40)
print(' TF-IDF')
print('-' * 40)

# jieba.add_word("手机壳", freq=None, tag=None)
s = '''衣服，汉语名词，读作（yī fu），是指人类或通过人类来完成遮掩身体、载体的用布料 
    （如棉布、丝绸、天鹅绒、化学纤维等）等材质做成的各种样式的遮挡物。 
    衣服在不同的场合有不同的穿着，样式非常的多，衣服在当今已经成为了不可或缺的东西，中国常说的“衣食住行”中排在首位。
    1.衣裳，服饰。
远达汉族传统服装
远达汉族传统服装
《诗[1]  ·小雅·大东》：“西人之子，粲粲衣服。”
《史记·赵世家》：“法度制令各顺其宜，衣服器械各便其用。”
宋 陆游 《老学庵笔记》卷二：“ 靖康 初，京师织帛及妇人首饰衣服，皆备四时。”
巴金 《灭亡》第一章：“街中聚集了一大群人，有着各样的身材，各样的衣服。”
2.借指形体，身躯。
宋苏轼 《答钱济明书》之二：“小人能害其衣服尔，至於其不可坏者，乃当缘厄而愈胜尔。”
3、穿衣服；使穿衣服。
《礼记·[2]  文王世子》：“﹝文王﹞鸡初鸣而衣服至於寝门外，问内竖之御者曰：‘﹝ 王季 ﹞今日安否何如？’”
宋 苏轼 《天篆记》：“ 江 淮 间俗尚鬼，岁正月必衣服箕箒为 子姑 ，或能数数画字。”[3] 
4、而今时尚的衣服那是令人眼花缭乱，不同的地区、不同的人群，各有各的观点，各有各的眼光，这也许是主观可的客观。
    '''

s2 = '''
随着科技水平的快速发展，科技美容这一行业做为新型产业新生而出。时尚IT品牌随着市场的多元化发展。针对手机品牌和功能的增加而呈多样化，将手机保护壳按质地分有PC壳，皮革，硅胶，布料，硬塑，皮套，金属钢化玻璃壳，软塑料，绒制，绸制等品类。手机保护壳不仅作为装饰品让您的手机成为一道风景，更能保护手机，防摔、防刮、防水和防震！
二十世纪九十年代中后期，手机壳借着移动电话瘦身的契机开始盛行。其种类也随着手机品牌和功能的增加而呈多样化，按质地分有皮革，硅胶，布料，硬塑，软塑料等品别。
手机壳发展到2013年，已不再是单纯的实用商品。随着手机在年轻群落中的普及，几乎每一个追求时尚的年轻人都希望拥有一部独一无二的手机。给手机美容逐渐成了他们展示个性的一种方式。
为了迎合这种趋势，手机保护套生产商又推出了许多做工更为精良，色彩图案更加别致的产品。这使得手机保护套的类型更加多元化。
1、保护手机作用，以防硬物在手机屏幕或机身上留下划痕。
2、手机壳上可以DIY上各种各样图案，有美容、时尚的作用！
3、硅胶壳可以防止指甲长时间与按键接触刮花、磨坏，有保护屏幕和按键的作用。
4、硅胶壳有防滑的作用。
手机外壳如此火爆，以苹果为代表的智能手机纷纷很多都可以换手机外壳，大量精力的外壳让人赏心悦目。皮质的、卡通的、金属的、磨砂的、镶钻的，这些琳琅满目的手机机壳市场售价从几十元到几百元不等，尤其定制自己照片深受客户喜爱。
手机壳打印机MINI版特点：个性定制，项目新潮，时尚， 配带移动电源，可流动经营。 市场前景广阔，有手机的都是客户。小巧mini，占地空间小; 便于携带，经营方式灵活;价格便宜，利于迅速开展业务。
可打印材质多，除普通手机壳外，还可直接在果冻壳 ，布丁壳，更多材质均可打印，如金属，TPU,PC，ABS,皮革等材质，玻璃制品，木制品上也可直接彩印。
手机保护壳可以分为：PC壳，硅胶、皮套、水晶壳、清水壳、网壳、环保PC外壳金属外壳、塑胶和碳纤维等。
'''

s3 = '''
调味品，flavouring;condiment;seasoning，是指能增加菜肴的色、香、味，促进食欲，有益于人体健康的辅助食品。它的主要功能是增进菜品质量，满足消费者的感官需要，从而刺激食欲，增进人体健康。从广义上讲，调味品包括咸味剂、酸味剂、甜味剂、鲜味剂和辛香剂等，像食盐、酱油、醋、味精、糖（另述）、八角、茴香、花椒、芥末等都属此类。
调味品主要是指香草和香料。香草是各种植物的叶子。它们可以是新鲜的、风干的或磨碎的。香料是植物的种子、花蕾、果实、花朵、树皮和根。香料的味道比香草浓烈得多。有些情况下，一种植物既能用于生产香草又能用于生产香料。有些调味品由多种香料混合而成（例如红辣椒粉），或者由多种香草混合而成（例如调味袋）。在饮食、烹饪和食品加工中广泛应用的，用于改善食物的味道并具有去腥、除膻、解腻、增香、增鲜等作用的产品。
罗勒： 新鲜或者风干的罗勒的甜味是意式菜肴的必备要素。
月桂叶： 整片风干的月桂叶可以为炖菜和肉类增添特殊的香气，不过请务必在上菜前拿走月桂叶。
细香葱：细香葱气味清淡，常用作菜肴的装饰。
莳萝：莳萝属于欧芹科，莳萝草是风干的、柔软且有茸毛的莳萝叶子。它特殊的香气很容易盖过菜肴的其他
味道，所以请慎用。
墨角兰：墨角兰的味道与牛至很接近，通常用于鱼类、肉类、家禽类的菜肴和番茄酱中。
薄荷： 薄荷既有新鲜的，也有风干的，可以用于蔬菜、水果类菜肴中，还可以用在茶里。
牛至：牛至的气味很重，极易盖过清淡的菜肴，但用在很多意式菜肴中却恰到好处。
欧芹：购买时，要选择鲜绿色且带有清新香气的欧芹。为便于储存，需仔细清洗欧芹，并甩去多余的水。先
用纸巾包裹欧芹，再将其放入塑料袋中。平时应冷藏，使用时再取出。欧芹常用作菜肴中的装饰。
迷迭香：尽管迷迭香不能很好地与其他香草配合，但特殊的香气使其成为肉类、家禽或烧烤的首选配料。
鼠尾草：新鲜鼠尾草的香气比风干的浓重许多，但两者都可以与野味、家禽和馅料很好地配合。
龙蒿：龙蒿常用于鸡类、鱼类和蔬菜中，也用于各种沙司中。新鲜龙蒿叶风干后辛辣味会大减。
百里香：百里香常用于蔬菜、肉类、家禽、鱼类、汤和奶油沙司中，为其增添风味。英国百里香是最受欢迎的一种。
多香果粉：这种香料有着肉桂、肉豆蔻、丁香的混合香气，因此而得名。
马槟榔：这些是马槟榔树上如豌豆大小的花蕾。马槟榔主要产于中美洲和地中海地区，可为沙司、调味汁和佐料增添辛辣的
卡宴辣椒：这种红辣椒需慎用，以免其味道过重，但对于很多拉丁美洲和西南部的菜肴来说是必备的。
红辣椒粉：和咖喱粉一样，红辣椒粉也是由辛辣的香料和磨碎的红辣椒混合而成。
肉桂粉：磨碎的树皮主要用于甜点，而整块树皮则可用于为苹果酒和其他热饮调味（味辣）。
丁香：这种甜味的香料既有整只的，也有磨碎的，常用于烤肉和甜点中。
孜然芹：磨碎的孜然芹因其辛辣的烟熏口味，常用于许多拉丁美洲和西南部的菜肴中。请慎用。
咖喱粉：咖喱粉由多种香料混合而成，包括姜黄、小豆蔻、孜然芹、胡椒、丁香、肉桂、肉豆蔻，有时还有
生姜。辣椒使它辛辣，磨碎的干大蒜则赋予它浓重的口味。咖喱是根据其不同的用途，选择不同的香料来混合的。
生姜：生姜是一种多节、棕褐色的块根，能为食物增添一种特殊的香气，广泛用于亚洲菜肴中。
肉豆蔻：这种香料带有辛辣的香气，以及一种温暖的、微甜的口味，常用于调味烘焙的食物、蜜饯、布丁、肉类、沙司、蔬菜和蛋奶酒。
红辣椒：磨碎的红辣椒能为土豆色拉和海鲜等菜肴增色，而又不使其过于辛辣。
干藏红花粉：这种芳香的香料主要用于汤和米饭中。
姜黄：和生姜一样，姜黄是咖喱粉的必备成分，一度被称为印度藏红花。请慎用——它只需一点，香气就足以持久。
按照我国调味品的历史沿革，基本上可以分为以下三代：
第一代、单味调味品，如：酱油、食醋、酱、腐乳及辣椒、八角等天然香辛料，其盛行时间最长，跨度数千年。
第二代、高浓度及高效调味品，如超鲜味精、IMP、GMP、甜蜜素、阿斯巴甜、甜叶菊和木糖等，还有酵母抽提物、HVP、HAP、食用香精、香料等。此类高效调味品从70年代流行至今。
第三代、复合调味品。现代化复合调味品起步较晚，进入90年代才开始迅速发展。目前，上述三代调味品共存，但后两者逐年扩大市场占有率和营销份额。
第四代、纯天然调味品。纯天然调味品以纯提前技术为前提，更以营养健康为重。目前，在益意追求健康为主的呼吁下，纯天然调味品所占领的市场份额越来越大。

调味品的每一个品种，都含有区别于其他原料的特殊成份，这是调味品的共同特点，也是调味品原料具有调味作用的主要原因。
调味品中的特殊成份，能除去烹调主料的腥臊异味，突出菜点的口味，改变菜点的外观形态，增加菜点的色泽，并以此促进人民食欲，杀菌消毒，促进消化。
例如：味精、酱油、酱类等调味品都含氨基酸，能增加食物的鲜味；香菜、花椒、酱油、酱类等都有香气；葱、姜、蒜等含有特殊的辣素;能促进食欲，帮助消化；酒、醋、姜等可以去腥解腻，调味品还含有人体必需的营养物质。如酱油、盐含人体所需要的氯化钠等矿物质；食醋，味精等含有不同种类的多种蛋白质，氨基酸及糖类，此外，某些调味品还具有增强人体生理机能的药效。
各种调味品基本上都有自己特定的呈味成份，这与其化学成份的性质有密切的联系，不同的化学成份，可以引起不同的味觉。我们常用的调味品主要呈咸、甜、酸、辣、鲜、香、苦等味。下面把可以引起各种味觉的化学成份分析一下。
1、咸味
咸味是化合物中，中性盐所体现的味道，如氯化钠，氯化钾、氯化铵等都有咸味，但同时又有其他异味。各种盐的呈味程度和化合物的分子量有关，分子量越大，苦味等异味越重。咸味的主要来源是食盐，食盐的主要成份是氯化钠，由于氯离子和钠离子的特有性质，决定了氯化钠有纯正的味道。
咸味调味品有盐、酱油、酱类制品。对一些肾脏患者，在生活中不能用食盐，可以苹果酸钠，谷氨酸钾代用。
2、甜味
甜味是普遍受欢迎的一种味型。甜味的产生主要是氨羟基等产甜味基因和助甜味基团共同作用的结果。聚合度较低的糖类物质，都有甜味，如蔗糖、麦芽糖、葡萄糖、果糖。
甜味调味品有：食糖（包括白糖、红糖）蜂蜜、饴糖、冰糖等。
3、酸味
酸味由有机酸和无机酸电离的氢离子所产生。食醋、番茄酱、变质的酱油和酒都可以作为酸味调味剂，常见酸味的主要成份是醋酸（乙酸）琥珀酸，柠檬酸，苹果酸，乳酸。有机酸，是一种弱酸，能参与人体正常的代谢，一般对人体健康无影响，能溶于水，其酸味远不及无机酸强烈。
4、辣味
辣味是一些不挥发的刺激成份刺激口腔黏膜所产生的感觉。其成份较复杂，各品种的辣味来源于不同的成份。
辣椒的辣味主要是辣椒碱；胡椒的辣味是辣椒碱和椒脂；生姜的辣味主要是姜油酮、姜辛素；葱蒜的辣味主要是蒜素。
5、鲜味
味精、鸡精、虾子、蚝油、虾油、鱼露等都有鲜味，虾子，蚝油，鱼露的呈鲜成份是各种、酰胺、氨基酸，味精是谷氨酸钠，鸡精是肌苷酸钠。
6、香味
香味来源于挥发性的芳香醇、芳香醛、芳香酮以及脂类等物质。
香味调味品有茴香、桂皮、花椒、料酒、香糟、芝麻油、桂皮酱、酱油、丁香花、玫瑰花等。
7、苦味
苦味来源于茶叶碱、可可碱，咖啡碱等生物碱有酮类化合物。粗盐中含有氯化镁，硫酸镁等也具有苦味。苦味食物有茶、咖啡、苦瓜、莲蕊等。
分类依据
中国研制和食用调味品有悠久的历史和丰富的知识，调味品品种众多。其中有属于东方传统的调味品，也有引进的调味品和新兴的调味品品种。对于调味品的分类目前尚无定论，从不同角度可以对调味品进行不同的分类：
按调味品商品性质
1、依调味品的商品性质和经营习惯的不同，我们可以将目前中国消费者所常接触和使用的调味品分为六类：
（1）、酿造类调味品：酿造类调味品是以含有较丰富的蛋白质和淀粉等成分的粮食为主要原料，经过处理后进行发酵，即借有关微生物酶的作用产生一系列生物化学变化，将其转变为各种复杂的有机物，此类调味品主要包括：酱油、食醋、酱、豆豉、豆腐乳等。
（2）、腌菜类调味品：腌菜类调味品是将蔬菜加盐腌制，通过有关微生物及鲜菜细胞内的酶的作用，将蔬菜体内的蛋白质及部分碳水化合物等转变成氨基酸、糖分、香气及色素，具有特殊风味。其中有的加淡盐水浸炮发酵而成湿态腌菜，有的经脱水、盐渍发酵而成半湿态腌菜。此类调泡发酵而成湿态腌菜，有的经脱水、盐渍发酵而成半湿态腌菜。此类调味品主要包括：榨菜、芽菜、冬菜、梅干菜、腌雪里蕻、泡姜、泡辣椒等。
（3）、鲜菜类调味品：鲜菜类调味品主要是新鲜植物。此类调味品主要包括：葱、蒜、姜、辣椒、芫荽、辣根、香椿等。
（4）、干货类调味品：干货类调味品大都是根、茎、果干制而成，含有特殊的辛香或辛辣等味道。此类调味品主要包括：胡椒、花椒、干辣椒、八角、小茴香、芥末、桂皮、姜片、 姜粉、草果等。
（5）、水产类调味品：水产类调味品水产中的部分动植物，干制或加工，含蛋白质量较高，具有特殊鲜味，习惯用于调味的食品。此类调味品主要包括：水珍、鱼露、虾米、虾皮、虾籽、虾酱、虾油、蚝油、蟹制品、淡菜、紫菜等。
（6）、其它类调味品：不属于前面各类的调味品，主要包括：食盐、味精、糖、黄酒、咖喱粉、五香粉、芝麻油、芝麻酱、花生酱、沙茶酱、银虾酱、番茄沙司、番茄酱、果酱、番茄汁、桂林酱、椒油辣酱、芝麻辣酱、花生辣酱、油酥酱、辣酱油、辣椒油、香糟、红糟、菌油等。
按调味品成品形状
2、按调味品成品形状可分为酱品类（沙茶酱、豉椒酱、酸梅酱、xo酱等）、酱油类（生抽王、鲜虾油、豉油皇、草菇老抽等）、汁水类（烧烤汁、卤水汁、喼汁、OK汁等）、味粉类（胡椒粉、沙姜粉、大蒜粉、鸡粉等）、固体类（砂糖、食盐、味精、豆豉等）。
按调味品呈味感觉
3、按调味品呈味感觉可分为咸味调味品（食盐、酱油、豆豉等）、甜味调味品（蔗糖、蜂蜜、饴糖等）、苦味调味品（陈皮、茶叶汁、苦杏仁等）、辣味调味品（辣椒、胡椒、芥茉等）；酸味调味品（食醋、茄汁、山楂酱等）、鲜味调味品（味精、鸡精、虾油、鱼露、蚝油等）、香味调味品（花椒、八角、料酒、葱、蒜等）。除了以上单一味为主的调味品外，大量的是复合味的调味品，如油咖喱、甜面酱、乳腐汁、花椒盐等等。
其他分法
4、调味品的分类还可以有其他一些方法，如按地方风味分，有广式调料、川式调料、港式调料、西式调料等；按烹制用途分，有冷菜专用调料、烧烤调料、油炸调料、清蒸调料，还有一些特色品种调料，如涮羊肉调料；火锅调料、糟货调料等；
另外，调味品的种类多，其中的一些产品有其专有的分类标准，如在中国，酱油可以分为酿造酱油、配制酱油。
'''

s4 = '''
休闲食品 (leisure food)其实也是快速消费品的一类，是在人们闲暇、休息时所吃的食品。最贴切的解释是吃得玩的食品．主要分类有：干果，膨化食品，糖果，肉制食品等．随着生活水平的提高，休闲食品一直是深受广大人民群众喜爱的食品。走进超市，就会看到薯片、薯条、虾条、雪饼、果脯、酸角糕、话梅、花生、松子、杏仁、开心果、鱼片、肉干、五香炸肉等休闲食品。休闲食品正在逐渐升格成为百姓日常的必需消费品，随着经济的发展和消费水平的提高，消费者对于休闲食品数量和品质的需求不断增长。
休闲食品可归纳为九大类：
谷物类制品(膨化、油炸、烘焙)
果仁类制品
薯类制品
糖食类制品
派类制品（酸角果派，西番莲果派等）
肉禽鱼类制品
干制水果类制品
干制蔬菜类制品
海洋类制品[1] 
在各种休闲食品中，一半以上的家庭曾经购买膨化食品，其次是饼干类食品。除此之外，口香糖和干果类休闲食品受到各类家庭的喜爱。
随着休闲食品种类越来越丰富，休闲食品正在逐渐成为人们日常生活中的必备品。随着国内市场的不断放
宽，越来越多的国际休闲食品品牌正逐步进入中国市场。伴随消费升级，我国休闲食品市场也呈现出由低端向高端发展的态势，整个食品体系逐步得到完善。2007-2011年，我国休闲食品总产值逐年上升，从2007年的20058.13亿元增至2011年的61185.20亿元，增长幅度较大。
2011年，我国休闲食品行业企业数量增加，产能提高，行业的销售利润和利润总额均较上年有所增长，休闲食品行业整体发展形势较好。根据国家统计局统计，2011年，我国休闲食品行业规模以上企业数量有4347家，实现销售额6114.05亿元，同比增长34.99%;实现产品销售利润814.53亿元，同比增长41.61%;利润总额为494.02亿元，同比增长40.32%;行业资产规模达到2905.32亿元，同比增长31.73%。
另据我国海关的数据显示，2011年，我国休闲食品行业进出口总额65.81亿美元，较上年增长37.38%，其中进口额37.35亿美元，较上年增长45.97%，出口额28.46亿美元，较上年增长27.52%，实现贸易逆差8.89亿美元，较上年增长171.83%。
但受欧美市场需求下降及国内经济增长放缓的影响，2012年1月，我国休闲食品行业实现出口额2.25亿美元较上年同期下降22.24%。
2012年1月，我国休闲食品行业进口额为1.70亿美元，较上年同期下降3.59%。其中，“供婴幼儿食用的零售包装食品”的进口额为6089.69万美元，占总进口额的35.74%，位居进口休闲食品之首。
公开数据显示，我国进口食品市场总额年平均增长率仍高达15%。据美国食品工业协会预测，到2018年中国将成为全球最大的进口食品消费国，届时中国大陆进口食品市场规模高达4800亿元人民币。
休闲食品行业在规模增长的同时，品种和类别也大幅度增多。市场上大行其道的休闲食品共有以下几大类：谷物膨化类、油炸果仁类、油炸薯类、油炸谷物类、食糖类、肉禽鱼类、干制果蔬类等。但中国休闲食品产量与国外发达国家相比相距甚远，尤其同世界休闲食品消费大国美国相比，中美两国人均消费差距约为150倍。另一方面，中国因几大休闲食品生产厂家都集中开发谷物膨化产品，使得产品品种单一，竞争较为激烈；由于技术力量相对薄弱，导致休闲食品风味还不能与国际上同类产品风味相媲美；国内除几大合资企业外，许多国营中、小型厂家制造的休闲食品包装色彩及品质较为粗糙；因技术力量不足、食品机械落后，使许多适龄产品的开发尚处空白。
我国的休闲食品零售业态主要有全国性食品零售连锁企业、区域性食品零售连锁企业、大型超市、地方性超市、食品零售店（便利店）、特产专卖店、个体小店、路边摊等，总体表现出零售业态多元化的特征。我国休闲食品零售行业有三类经营模式，即个体经营的零售模式、超市卖场零售模式、连锁零售模式。
（1）个体经营的零售模式
主要是以个体门店为销售渠道，其主要特点为无品牌、无包装零售。由于目标市场消费人群对于质量、口味及品牌要求的提高，此类模式市场份额逐步减小。
（2）超市卖场零售模式
一些生产型休闲食品企业主要采用超市卖场零售模式，即通过独立包装的休闲食品，借助以大卖场、超市及遍布大街小巷的便利店为主的销售渠道推广自己的产品。我国这种经营模式是我国休闲食品的主要销售模式。
（3）连锁零售模式
连锁零售模式为主要以连锁专卖店形式专业化销售多种类休闲食品的经营模式。连锁零售模式采用统一采购、统一配送、统一管理、统一形象，让管理更有效率、品牌更突出、服务更便捷、产品线更丰富、价格更实惠，产品也更具有市场营销竞争力。
随着人们生活水平的不断提高，原来以温饱型为主体的休闲食品消费格局，逐渐向风味型、营养型、享受型甚至功能型的方向转化。尤其随着市场的不断扩大，休闲类食品市场开始快速发展，而且呈现出一片前所未有的繁忙景象。
市区一家大型超市负责人向记者表示，随着休闲食品消费的繁荣，更多的人已将着眼点放在了健康和营养方面。休闲食品生产厂商正在宣传休闲食品可以成为健康平衡膳食的一部分——低热量、低脂肪、低糖的休闲食品是今后新品开发的主流。随着休闲食品行业的发展以及人们生活水平的提高，休闲食品开始贴近人们的生活。
据超市相关负责人介绍，休闲食品市场规模呈几何级的速度增长，高出食品市场平均增长率20个百分点。但面对世界经济的一体化，休闲食品市场却略显底气不足，面临着严峻的挑战。业内人士指出，随着休闲食品产业规模的扩大，一些有实力、有品牌的优势企业必将占据垄断地位，形成企业优势和地域优势，从而使红火的休闲食品市场走向规范。
某超市休闲食品销售人员告诉记者，虽然，休闲食品市场日益红火，但是，流通渠道单一，购买休闲食品的场所主要是超市及便利店，其次是大卖场、食品店、杂货店等。搭建新的营销平台，增强企业自主营销意识，成为休闲食品产业发展新的需求。休闲食品是具有旺盛生命力的产品，有着广阔的市场和巨大的发展潜力。同时，由于食品行业已经进入完全竞争阶段，企业利润日趋平均化，行业整合、市场细分即将完成，因此，休闲食品企业应抓住机遇，扬长避短，通过新产品开发、品牌建设和市场拓展，通过差异化战略，走出一条快速、健康、可持续发展的道路。
2005-2016年休闲食品市场规模
2005-2016年休闲食品市场规模
休闲食品能减轻人的心理压力，并能帮助食用者缓解自身情绪，保持心情舒畅，休闲食品逐渐成为人们日常消费必不可少的一部分。中国产业经济研究网调查显示，即使在受金融危机影响的2008-2009年，休闲食品行业受到的冲击依然很小，国人对休闲食品的需求也呈现出不减反增的势头。虽然2011年我国休闲食品市场容量已高达960亿元以上，但人均消费量远低于发达国家人均消费水平。随着我国经济水平及人们消费水平、购买能力的不断提高，休闲食品市场仍将会高速增长，我国休闲食品企业在未来具有巨大的发展空间。
商店里休闲食品是琳琅满目，供大家选择的也是数不胜数，但是在选择和使用休闲食品的时候，要学会为自己的人身和健康着想，为此向广大休闲食品消费者提供以下有用的建议
硬果类
包括：花生、松子、榛子、杏仁、胡桃、开心果、白瓜子、葵花子、西瓜子等。
安全隐患：霉变、受潮、虫蛀。
专家支招：很多硬果类食品都是散装的，可以通过品尝来判断是否有质量问题。对于包装好的硬果类食品，可以通过观察硬果的外观来分辨好坏。高质量的硬果，一般色泽都比较鲜亮，有光泽，干燥无杂物，不会出现霉斑、虫眼等。因此，在购买时，一定要认真仔细地检查包装袋里的硬果是否有“问题”。
膨化类
包括：虾条、薯片、爆米花、雪饼、虾酥等。
安全隐患：添加过量防腐剂、保存不当造成细菌污染、超过生产日期。
专家支招：据介绍，为了使膨化食品外形美观、保存方便，不少厂家在包装袋内冲入气体，有的甚至滥用膨化剂等成分。而这些气体和膨化剂一旦加入过量，势必造成食品中含有的有害成分增多，危害人体健康。因此，选购膨化类食品时，一定要选择品名、配料、厂家地址、生产日期、保质期等标识齐全、明确的产品，尽量不要在一些路边店、小地摊等没有质量保证的地方购买。同时，注意这类食品是否干脆新鲜。
果冻类
包括：果冻、果脯、果丹皮、话梅等。
安全隐患：滥用色素、化学成分残留、超市二次污染。
专家支招：专家指出，果冻果脯类食品中会含有香精、防腐剂等成分，过多食用或者食用不合格产品，会对身体造成很大危害。专家建议，购买果冻果脯类食品时，一定要选择名牌产品，选择知名厂家。同时，颜色过于鲜艳、有刺激性气味、包装过于简单、生产日期等标注不明的产品一定不要购买。
肉干类
包括：鱼片、肉松、牛肉干、猪肉干等
安全隐患：假冒伪劣、色素过多、肉质不良、细菌污染、防腐剂超标。
专家支招：不合格的肉干肉脯类食品中往往色素过多，而且含有大量化学成分，有的甚至含有致癌物质，食用后对身体危害很大。因此，消费者在购买时首先要确定密封包装，没有破漏和缝隙。同时要注意查看肉干肉脯的色泽和外观，高质量的肉干肉脯应该色泽鲜艳、肉质鲜嫩，香味纯正，没有异味。选择肉松时则要注意，好的肉松质地蓬松柔软，有弹性，不含肉筋碎骨等，嚼碎后没有渣滓。
美国营养学家研究证明了一个惊人的结果：在某种意义上，贪吃零食和受到辐射一样会让人易患癌症。这是因为，人体的遗传物质——DNA的合成与修复需要叶酸、维生素B12、维生素B6、维生素C、维生素E等营养素，如果这些营养素不足，会导致DNA损伤无法修复，其后果与辐射带来的伤害非常相似。
人们重视维生素，主要是因为它能够预防坏血病、脚气病等营养素缺乏症。许多调查也证明，与营养良好的人相比，缺乏维生素A、维生素B2、维生素C、维生素E的人更容易患癌症，包括肺癌、胃癌、乳腺癌、宫颈癌等。
人体每天对维生素的需要量很小，不能靠食欲感觉到维生素的不足。随着工作节奏的加快和食品的丰富，生活中很容易发生维生素的缺乏。这是由于大部分零食、饼干、薯片、糖果、巧克力、甜饮料和方便食品所含的维生素都很少。然而，许多人上班前没时间吃早饭，早上用饼干凑合，中午吃方便面，晚上以速冻食品解决；饥饿时大吃零食，渴了便求助于甜饮料，势必造成维生素缺乏的状况。特别是脑力劳动者，消耗的维生素数量更多，更需要注意及时补充。
发霉的花生不能吃——黄曲霉素是引起胃癌，肝癌，食道癌的罪魁祸首，它是由发霉的粮食，花生所长出的黄曲霉菌产生的。所以，发霉的粮食，花生千万不能吃。
绿色休闲食品具有两方面的含义：一是作为原料的农产品是在自然赋予的、不含有农药化肥的自然环境下生长的，普遍具有绿色、有机等特点；二是食品加工过程中尽量不添加食品添加剂，产品保持了原料的原质、原味、原形，是一种纯天然的绿色食品。市场上主要绿色休闲食品有甘薯制品、板栗制品、枣制品、山楂制品、豆制品等。

随着我国旅游行业的兴旺发展，休闲食品尤其是绿色休闲食品进入不断改进和创新的发展新阶段。我国绿色休闲食品市场迅速发展，2009年市场规模90亿元，2010年增长至123.5亿元，预计2014年将达到363.7亿元，在中国食品市场的地位日益重要。
对于已经处于该市场中的企业主，应该把握市场趋势，加紧开发新产品；而对那些即将进入该市场的投资者，则应该了解市场信息，做好投资决策。
虽然相对于外资企业，本土企业在生产技术、新产品开发以及品牌建设等方面比较落后。但是我们仍然可以看到在渠道下沉方面，本土企业具有与生俱来的优势。外资品牌多为全国性品牌，在一线城市中主要依靠全国化、规模化的大型连锁超市等现代流通渠道，通常采取与超市直接签订进场协议或者通过区域内较大的经销商进场，流程相对规范，规模效应强。但是我国三四线城市和乡镇农村的零售业态还主要以传统流通渠道为主，如地方性超市和食品零售店等，外资品牌要进入这一市场需要通过当地经销商，这些经销商一般规模较小，运营成本较高，很难形成规模效应。而本土企业一般都是从区域品牌成长起来的，对于运作三四线城市及农村市场有优势和经验，更善于与传统流通渠道经销商打交道，终端覆盖率随着区域级别的降低而更容易提升。目前我国零售终端中90%以上都是传统渠道的终端，未来随着渠道下沉，本土企业将在渠道深耕上发挥更大的优势。

一、膨化食品
雪饼、薯片、虾条、虾片、鸡条、玉米棒……这些食品色彩鲜艳，包装醒目，广告宣传引人注目，赢得了孩子们的青睐。
膨化食品不合格产品的主要问题是细菌污染，如大肠菌群超标，以及膨化食品中所含脂肪腐败而引起的过氧化值升高。这些会导致孩子胃肠不适、腹泻和肝脏损害。国家和地方质量技术监督部门定期会进行一些检测，爸爸妈妈要注意有关信息，避免买不合格的产品。
选购膨化食品时，要选择品名、配料表、净含量、厂名、厂址、生产日期、产品标准和保质期等标识标注齐全的产品，并尽量到一些信誉比较好的大商场、大超市购买。
为了防止膨化食品被挤压、破碎，防止产品油脂氧化、酸败，不少膨化食品包装袋内要充入气体。欧美国家有法规规定，要求膨化食品一律充装氮气，它清洁、无毒、干燥，能保证膨化食品长期不变色、变味，食用安全。
但我国因无相关法规，有不少厂家用的是压缩空气，压缩空气的含水量比正常空气高，会造成袋内膨化食品口感不酥脆，并且在压缩空气的过程中，还有可能将机器内注入的润滑油化作雾态，喷入包装袋内，附着在包装袋内壁，沾在膨化食品上。
　　所以，在购买膨化食品时，若发现包装袋上标注有充装氮气的字样，就可以放心了。若发现包装泄气，则不宜选购。
提醒：许多小朋友都喜爱膨化食品。脂肪、碳水化合物、蛋白质是膨化食品的主要成分。膨化食品虽然口味鲜美，但从成分结构看，属于高油脂、高热量、低粗纤维的食品。
从饮食结构分析有其一定的缺陷，只能偶尔食之。长期大量食用膨化食品会造成油脂、热量吸入高，粗纤维吸入不足。若运动不足，会造成人体脂肪积累，出现肥胖。孩子大量食用膨化食品，易出现营养不良，而且膨化食品普遍高盐、高味精，将使孩子成年后易导致高血压和心血管病。
二、饼干
饼干分为酥性饼干、薄脆饼干、曲奇饼干、夹心饼干、威化饼干、蛋卷等种类。消费者在购买时应首选大型超市、知名企业生产的产品；二是要选购包装质量好的产品，好的产品包装可避免流通过程中引起的二次污染；三是要选购在保质期内的产品，最好是接近当天生产的产品。
二、果冻
果冻是广大儿童喜爱的食品，由于其产品利润丰厚，加工相对简单，因此不少小企业纷纷加入生产队伍，使该类产品得以迅速发展，同时也带来了产品质量参差不齐的问题。
在选购果冻时，一要选择品名、配料表、净含量、厂名、厂址、生产日期、产品标准和保质期等标识标注齐全的产品，并尽量到一些信誉比较好的大商场、大超市购买，以保证买到质量较好的产品；
二要看果冻的颜色，那些色彩鲜艳的果冻往往是添加了较多的色素，虽然很诱人，但孩子食用过多对身体是有害的；三要看配料中是否添加了防腐剂和甜味剂，产品中的防腐剂和甜味剂属于人工合成的添加剂，食用过多也是有害的。
三、糖果
选购糖果时，应从以下几个方面着手：糖果的外观，色泽应正常、均匀、鲜明，香气纯正，口味浓淡适中，不得有其他异味;糖果的外型应端正，边缘整齐，无缺角裂缝，表面光亮平滑、花纹清晰，大小厚薄均匀，无明显变形;糖果应无肉眼可见的杂质。
硬糖：坚脆型糖果的组织表面应光亮透明，不粘包装纸，无大气泡和杂质;酥脆型糖果应色泽洁白或有该品种应有的色泽，酥脆，不粘牙，不粘纸，剖面有均匀气孔。
奶糖：胶质型糖果应表面光滑，口感细腻润滑、软硬适中，不粘牙，不粘纸，有弹性;非胶质型糖果表面细腻，结晶均匀，不粗糙，软硬适中，不粘牙，不粘纸。
软糖：琼脂型糖果柔软适中，不粘牙，无硬皮，其中水晶软糖光亮透明，不软塌，略有弹性，花色软糖表面有密布均匀的细砂糖，柔嫩爽口。如酸角糕、西番莲果派等。
果胶淀粉型糖果口感韧软，不粘牙，不粘纸，略具咀嚼性，糖表面附有均匀的细砂晶粒，糖体半透明，其中的高粱饴具有弹性，拉长一半可缩回原状;明胶型糖果表面平滑细腻，无皱皮气泡，富有弹性，入口绵软。
夹心糖：酥心型糖果糖皮厚薄均匀，不粘牙，不粘纸，无破皮露馅现象，疏松酥脆，丝光纹道整齐，夹心层次分明;酱心型糖果糖皮厚薄均匀，不粘牙，不粘纸，无破皮露馅现象，皮脆，馅心细腻;粉心型糖果糖皮厚薄均匀，松脆，不粘牙，不粘纸，不破皮漏心。
纯巧克力糖：表面光滑，有光泽，不发白，剖面紧密，无1毫米以上明显的气孔，口感细腻润滑，不糊口，无粗糙感。
夹心巧克力糖：表面光滑，有光泽，不发白，涂层均匀，不过厚或过薄，各种夹心巧克力糖有自己的独特味道。
提醒：生病的宝宝少吃糖。吃甜食多，会对病儿免疫力产生不利的影响，“甘能伤脾”这一中医论点，讲的就是这个道理。正常情况下，人体血液中一个白血球的平均吞噬病菌能力为14，吃了一个糖馒头之后变为10，吃了一块糖点心之后变为5，吃一块奶油巧克力之后变为2，喝一杯香蕉甜羹后则为1，足可见甜食对免疫力的危害。
'''
for x, w in jieba.analyse.extract_tags(s4, topK=1000, withWeight=True):
    print('%s %s' % (x, w))

print('-' * 40)
print(' TextRank')
print('-' * 40)

for x, w in jieba.analyse.textrank(s4, topK=1000, withWeight=True):
    print('%s %s' % (x, w))
