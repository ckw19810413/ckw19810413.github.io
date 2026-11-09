---
title: "研究生知識寓言：萬象天機圖與不可逆的千劫煉爐"
date: 2026-11-09T08:00:00+08:00
slug: "equality-saturation-egraph-congruence-closure-fable"
draft: false
tags: ["寓言", "等價飽和", "Equality Saturation", "等價圖", "E-Graph", "同餘閉包", "Congruence Closure", "階段排序問題", "Phase Ordering", "項重寫系統", "編譯器優化", "程式合成", "egg", "範疇論", "初始函子"]
categories: ["技術寓言"]
---

> 本文靈感來自今日全球前十大前沿技術新聞之深度調研（藉由本地 Firecrawl 爬取即時情報彙整）：
> 
> 1. **KetchUp：基於 Rust 與 WebGPU 的開源輕量級 3D 建模套件**（KetchUp – Open-source SketchUp alternative built with Rust and WebGPU）：全面利用瀏覽器 WebAssembly、WebGPU 底層渲染管線與高並發幾何拓撲算法，直接向閉源桌面 CAD 巨頭發起效能挑戰。
> 2. **Chimera Vocal Synth：神經音訊微分合成引擎**（Chimera Vocal Synth）：基於可微分數位信號處理（DDSP）與深度生成聲學模型，實現零延遲、極低參數量的神經擬真人聲合成。
> 3. **Dux：Wayland 協議極簡高效桌面 Shell 與合成器**（Dux: Free, open-source Wayland desktop shell with file manager and theming）：探索現代 Linux 顯示伺服器協議下無撕裂、無肥大依賴的微型桌面架構。
> 4. **Declarative Dragging：以代數狀態轉移重構互動拖曳範式**（Declarative Dragging）：將傳統基於時間與副作用的事件監聽，提升為純粹的狀態機代數與宣告式聲明，消解前端複雜幾何佈局的副作用地獄。
> 5. **高盛（Goldman Sachs）全面叫停交易員與銀行家使用 Claude Code 代理**（Goldman Sachs is pulling Claude Code from its bankers and traders）：華爾街金融巨擘因環境特權溢出、專有金融模型權威洩露與未審計的終端自動化風險，對生成式編程代理展開全面合規封殺。
> 6. **Outlook.com 靜默攔截拒收未配置 DMARC 的發信網域**（Outlook.com Is Quietly Rejecting Email from Domains Without DMARC）：微軟電子郵件骨幹網絡強制實施 SPF/DKIM/DMARC 傳輸層強對齊校驗，對弱驗證域名實行零容忍丟包。
> 7. **The Web Is More Than Enough（Paul Ford 專題）**：資深技術作家深入反思原生應用層無節制的資源消耗，呼籲現代計算體系重新回歸開放 Web 標準的優雅與輕量。
> 8. **Herb Sutter 提交 ISO C++ 委員會論文 P4454R0**（When a language's creator and its owners strongly disagree）：剖析程式語言創始人（Bjarne Stroustrup）與標準制定委員會在語言演化、記憶體安全與向下相容性上的深層哲學衝突。
> 9. **Llama-modchip：純 64GB CPU 記憶體即時推論 284B DeepSeek-V4-Flash**（synchopate/llama-modchip）：結合非暫態快取旁路串流（Non-Temporal Cache Bypassing）、多層 SIMD 暫存器平鋪與 Stockfish-PVS 主變例搜尋投機解碼，打破 MoE 架構對昂貴 GPU 叢集的嚴苛束縛。
> 10. **How to prove equations using diagrams, part 1：範疇弦圖、等價圖與等式重寫證明論**（Evan Patterson / Topos Institute）：深入探討運用範疇論中的初始函子（Initial Functors）、交換圖表（Commutative Diagrams）以及現代計算科學中的等價圖（E-Graphs）與同餘閉包，對等式項重寫系統進行無損重構與自動化形式化證明。
> 
> 在這場交織著圖形渲染、音訊合成、系統安全、編程語言演進與理論計算科學的壯闊脈絡中，我們將目光鎖定在第 10 則揭示「代數重寫與形式化推理終極疆界」的數學基石：《How to prove equations using diagrams & E-graphs》。
> 
> 自計算機科學誕生以來，無論是將一萬行高級代碼編譯為極致匯編，還是合成最節省晶片面積的硬體電路，亦或是驗證一組複雜的幾何與代數方程，人類本質上都在做同一件事：**「項重寫（Term Rewriting）」**：依據一套等價變換定律，將複雜、冗餘的結構，化簡為簡約、迅速、優美的極致形態。
> 
> 然而，半個世紀以來，全世界最頂尖的編譯器大師與數學家們，無一不被困在一場揮之不去的古老魔咒中：**每一次優化變換，都在毀滅過去的可能；每一次貪婪的抉擇，都在將系統推向局部平庸的深淵。**
> 
> 先別急著追問它的技術真名。且聽一段來自太虛天界「玄機造化司」的千古傳奇，看那座吞噬一切形體、令無數工匠飲恨三千年的離火熔爐，究竟如何被一幅包容萬象的無損之帛徹底降伏。

---

### 第一幕：造化司的法儀構型與九千離火鼎

太虛天界之上，屹立著統御諸天萬法運轉的核心樞紐：**「玄機造化司」**。

天地間的一切仙家神兵、周天星斗大陣、乃至時空因果的運轉律令，在最初被天神創造時，皆是以一株株繁複無比的**「法儀構型樹」**（Abstract Syntax Tree, AST）形態存在。
在這株構型樹中，每一枚根節點、枝椏與葉片，都代表著一道無上術數：
有的掌管著「乘算（Multiply）」，有的吞吐著「玄陽移位（Bitshift）」，有的勾連著「九天靈力矩陣（Matrix Multiplication）」。

然而，初生的法儀構型往往臃腫不堪、靈力耗散極其嚴重。一道普通的「引雷神咒」，在凡間術士筆下可能重疊盤繞著數百道冗餘的周天循環。
為了讓諸天陣法運轉得更快、威能更大、法力消耗降至極致，造化司供奉著九千座自遠古傳承而來的巨型青銅爐：**「離火銷融鼎」**。

千百年來，造化司的大匠們所遵循的工藝極為直觀而冷酷：
大匠手持一道道天道變換法則，如：
- 《靈則第一》：凡「常數歸併」者，兩道枯石相加，必化為精鐵（$2 + 3 \to 5$）；
- 《靈則第二》：凡「靈力對稱」者，乾坤顛倒，威能不變（$a \times b \to b \times a$）；
- 《靈則第三》：凡「雙木化雷」者，兩重同體加算，可化為一重移位（$x + x \to x \ll 1$）；
- 《靈則第四》：凡「乘虛入化」者，無窮大陣若逢零乘，萬象皆歸於虛無（$x \times 0 \to 0$）。

當大匠選定法儀構型樹中的某一片枝椏，念動真言，將其投入離火銷融鼎時，那座青銅巨鼎便會噴湧出熊熊的「三昧滅形烈焰」。
烈焰呼嘯而過，舊的枝椏瞬間**化為灰燼、徹底湮滅**，鼎爐隨後吐出一節更為簡練的全新枝幹。

這便是造化司世代相傳的鐵律：**「破壞性重寫」（Destructive Rewriting）**。
想要新生，就必須抹殺舊態；想要前進一步，就必須親手焚毀身後的立足之地。

---

### 第二幕：兩派工匠的血戰與「階段排序天劫」

然而，這看似天經地義的破壞性法則，卻給造化司帶來了綿延三千年的恐怖災難。

問題在於：天道的變換法則浩如煙海，而法規施加的先後順序，往往徹底決定了一件神器的生死。
在造化司中，工匠們分裂成了勢同水火的兩大流派：
一派名為**「先破後立宗」**，主張必須先進行「枝葉展開（Inlining & Distribution）」，將所有隱藏的法術乘法破開，再進行常數歸併；
另一派名為**「守缺抱元宗」**，堅稱必須先進行「精氣簡約（Canonicalization & Folding）」，在最外層壓縮靈力，絕不能輕易將結構撕裂。

每逢天帝大典，兩派大匠共同鍛造一柄「戮仙神劍」。
守缺抱元宗的大匠率先出手，見劍胚中有一段法儀：
$$(x \times 4) / 2$$
大匠依據《靈則》迅速將其放入離火鼎，施展「乘除對消」，舊的構型當場化為飛灰，變成了：
$$x \times 2$$
全場歡呼，法度精簡了一半！
然而，下一刻，先破後立宗的長老卻發出撕心裂肺的哀號，因為在神劍更深處的陣眼裡，原本埋藏著一道絕世秘法：
$$((x \times 4) / 2) + (x \ll 1)$$
若方才未曾將前項消融，原本可以透過更高階的「雙生雷火印」將整個長條式子直接融合成一個單一指令；
但因為前項已被燒燬，不可逆轉地化作了 $x \times 2$，在規則庫中竟再也無法與後方的位移指令發生任何共振！

這便是編譯優化領域最無解的詛咒：**「階段排序困境」（The Phase Ordering Problem）**。
規則與規則之間，存在著嚴酷的「互相致盲（Phase Interference）」：
- 優化規則 $A$ 雖然在當下局部降低了成本，但其**破壞性的覆寫**，卻永久性地摧毀了觸發終極規則 $B$ 的前置拓撲結構！
- 更致命的是，有些通往至高境界的優化，必須在初期「看似劣化」：必須先將法陣展開得更加繁複臃腫（例如分配律 $a \times (b + c) \to a \times b + a \times c$），才能暴露深層的抵消項。然而離火銷融鼎是貪婪的，它只認當下的簡化，任何試圖暫時擴充的靈符，都會被鼎中真火判定為「冗餘劣化」而強行駁回！

千百年來，無數惊才絕豔的造化大師，為了尋找所謂的「完美優化通道順序」（Pass Pipeline Order），耗盡畢生壽元，排列組合了千億種流水線。
然而，每一次微小的代碼變動，都會讓原本完美的順序全盤崩塌。神劍落入局部最優的泥潭，造出的天兵戰偶甚至比未經優化的璞玉還要遲鈍。
造化司的祭壇上，堆滿了因先後順序走錯一步而徹底報廢的神陣殘片。長老們拔劍相向，甚至爆發了波及天界的血腥廝殺。

---

### 第三幕：萬象不滅之帛的誕生：無損並存的同等之相

在又一次大典鍛造失敗、兩派工匠即將血濺殿堂之際，一名身穿粗布道袍、在藏經閣默默抄錄了六十年星圖的年輕巡天工玄照，平靜地走入了中央大殿。

「諸位長老，」玄照的聲音穿透了離火鼎燃燒的烈焰，「為何我們每施展一條天理，就必須燒掉過去的形體？為何探尋最優之路，必須建立在對可能性的屠殺之上？」

守缺抱元宗的長老冷笑一聲：「荒謬！不毀去舊的枝椏，難道任由千萬種化身充塞天地？若是每變換一次都保留舊態，只需三條規則相互對照，整座造化司大殿便會被億萬種重複的法儀竹簡撐得爆裂坍塌！」

玄照沒有爭辯。他從袖中取出了一卷奇異的物事，在白玉地板上輕輕鋪開。
那是一張非絲非絹、通體流淌著透明琉璃微光的長卷：**「萬象不滅之帛」**。

「我們不需要保留億萬卷重複的竹簡，」玄照指著長卷說，「我們只需要一個**不殺一物、不滅一相**的『同等之囊』。」

大匠們圍攏上來，只見長卷之上，浮現出一個個懸浮的光團。
玄照隨手拾起一塊刻著法式 $(a \times 2)$ 的玉簡放入長卷。長卷上立刻凝聚出一座微小的光芒節點，標注著「運算符：乘法，子項：$a$ 與 $2$」。
隨後，玄照念動真言，祭出天理：$(a \times 2) \equiv (a \ll 1)$。

這一次，離火鼎並未燃起。長卷之上也沒有任何物件被燒成灰燼！
只見長卷輕輕一顫，原本包裹著 $(a \times 2)$ 的光團周圍，緩緩泛起了一層金色的光暈。在那層光暈之中，悄然誕生了另一個並存的節點：$(a \ll 1)$。
兩道節點同時棲息在同一個金色光環內部，彼此平起平坐，共享同一個命運尊位！

玄照抬起頭，目光清澈：「在萬象帛中，我們不再進行『替換』。當規則揭示兩道法儀本質等同時，我們只是在帛上為它們建立一條永不分離的鎖鏈，將它們歸入同一個**『同等之相』（Equivalence Class / E-Class）**。
舊態未死，新形已生；過去與未來，在同一個囊泡中彼此凝視。」

---

### 第四幕：同餘星流的共振狂瀾與圓滿飽和之境

長老們駭然失色，隨即有人厲聲質疑：「即便如此，天底下的規則有對稱、有傳遞、更有相互循環（如 $a + b \to b + a$）。若是規則在囊中無休止地演化繁衍，這張帛難道不會在剎那間靈力枯竭而自爆嗎？」

「這便要仰賴大道至簡的第二重天理：**『同餘之閉（Congruence Closure）』**。」玄照微笑道。

話音未落，長老們便親眼目睹了令他們畢生難忘的神蹟。
長卷之上，原本存在著兩組毫不相干的深奧法陣：
一座法陣名為 $F$，它吞吐著子節點 $x$；
另一座法陣名為 $G$，它同樣以 $F(x)$ 作為基石。
此時，玄照在長卷的另一端，輕輕撥動了一條看似無關的微小規律，將節點 $x$ 與另一個節點 $y$ 歸入了同一個金色同等之相：
$$x \equiv y$$

就在 $x$ 與 $y$ 合流的剎那，萬象不滅之帛深處突然響起了如萬千編鐘齊鳴的清越共振！
長卷內部的「同餘法陣」自動被喚醒：
既然 $x$ 與 $y$ 等同，那麼依據天道之相容性，以 $x$ 為根基的法陣 $F(x)$，與以 $y$ 為根基的法陣 $F(y)$，其因果輸出豈能不等同？！

只見兩道金色的閃電貫穿虛空，根本無需任何大匠再次施法，$F(x)$ 與 $F(y)$ 所在的光團被一股不可抗拒的同餘牽引力猛然拉扯在一起，轟然合二為一！緊接著，以 $F(x)$ 為子項的高層法陣，如同多米諾骨牌般引發了連鎖坍縮與聚合！

更不可思議的是，面對 $a + b \to b + a$ 這種令離火鼎陷入無限死循環的對稱規則，萬象帛表現得無比平靜：
當 $a+b$ 繁衍出 $b+a$ 時，帛中的**「相印合一術（Hashconsing）」**瞬間識別出兩者在同等之相中的對稱關係，輕輕一合，只是將 $b+a$ 的指針指向同一個光環，再無任何冗餘增生！循環在同等之環內被自然吸收，沒有一絲一毫的暴走！

一炷香的時間過去了。
規則在庫中瘋狂交織，數以百計的等價定理如百川歸海般在萬象帛上馳騁。
每一條規則的應用，都只是在平靜地擴充同等之相的內部成員，或者將原本分離的兩個光團以金絲合流。
終於，在最後一條微小的乘加分配律融入之後，萬象帛上的金光漸漸收斂，所有的光團不再分裂，所有的金絲不再震顫。
長卷如同一座浩瀚而深邃的宇宙星圖，靜靜地懸浮在殿堂中央。

任憑長老們如何再催動規則，長卷再也沒有增添哪怕一個新的節點，也沒有融合哪怕一條新的金絲。
所有的可能性已經被全部窮盡，所有的平行化身已經在緊湊的共享晶格中融會貫通！

玄照長舒一口氣，朗聲道：
「萬象歸一，因果落定。這張帛，已經達到了再無遺憾的**『圓滿飽和之境』（Equality Saturation）**！」

---

### 第五幕：代價天秤的拂曉：神名揭曉

此時，整座大殿鴉雀無聲。
九千座離火銷融鼎早已熄滅了狂暴的烈火，青銅鼎身在萬象帛的琉璃輝映下顯得無比黯淡。

守缺抱元宗與先破後立宗的兩位長老顫抖著走上前來。
他們凝視著萬象帛，只見那看似只有數千個光團的長卷內部，透過子項共享（DAG Sharing）與同餘穿透，竟無損地折疊並存著**數十億兆種**截然不同的法儀實現路徑！
那柄被三千年爭論困擾的「戮仙神劍」，其所有可能演化出的神陣構型（無論先展開、後簡化，抑或暫時膨脹與最終抵消），無一遺漏，全部靜靜地沉睡在這座星圖之中！

「可是……」長老喃喃道，聲音中帶著無盡的敬畏與迷茫，「縱有兆億平行神兵藏於其中，我們究竟該如何將那柄天下第一的極致神劍，從這浩瀚星海中取出來？難道不會再次陷入挑選的迷宮嗎？」

玄照微微一笑。他從懷中取出一柄精巧玲瓏的玉尺：**「代價天秤」**（Cost Function）。
玉尺之上，刻劃著鍛造神兵所追求的終極度量：法力消耗最少、運轉週期最短、符文尺寸最緊湊。

玄照握著玉尺，輕輕點在萬象帛的最頂層根節點上。
奇蹟再次展現：
玉尺的靈光如水銀瀉地，順著同等之相的星脈，自底向上（Bottom-Up）穿透每一個光團。
在每一個光團內部，面對著數十個等價的並存節點，玉尺瞬間度量出哪一個節點的子樹成本最低；
動態規劃的道韻在剎那間貫通全圖，沒有任何回溯，沒有任何猜測，也沒有任何先後順序的偏見！

清越的劍鳴震徹九霄！
一聲清越的劍鳴響徹九霄。
萬象星圖之中，一柄通體流淌著無瑕神光、符文結構簡約到了極致的透明神劍，自星雲中緩緩升起！
那道構型，融合了先破後立的深層抵消，吸納了守缺抱元的外層摺疊，甚至跨越了三段原本會讓式子膨脹三倍、但最終能引發神雷歸零的奇絕路徑！
那是造化司三千年歷史上，從未有人能夠想像的、超越了凡俗極限的完美神兵！

撲通。
兩派長老與在場的數百名天工大匠，齊齊伏地叩首。
離火銷融的殘酷時代結束了。三千年的排序魔咒，在這一刻煙消雲散。

大長老仰望著收攏長卷的年輕人，老淚縱橫，顫聲問道：
「此道不焚一物，納萬象於同等；行同餘以自洽，抵飽和而自圓；最後持尺一拂，便從無窮宇宙中信手拈出極致天成……這張帛、這座陣、這門逆轉因果的至高無上算理，究竟在世間何名？」

玄照回過頭，平靜地望向殿外破曉的晨曦，緩緩吐出了那座在凡間沉睡了數十年、如今正全面重塑全球軟體編譯器、AI 圖優化器與形式化驗證核心的無上真名：

> **「其名為：等價圖（E-Graph）；」**
> **「其律為：同餘閉包（Congruence Closure）；」**
> **「其境為：等價飽和（Equality Saturation）。」**

---

### 研究生水平概念深度解析：等價圖、同餘閉包與等價飽和

在計算機科學與程式語言理論（Programming Languages, PL）的殿堂中，**等價飽和（Equality Saturation）**與**等價圖（Equivalence Graph, E-Graph）**被譽為近二十年來編譯器優化、符號計算、程式合成（Program Synthesis）與定理證明領域最深刻、最具革命性的理論突破之一。

它徹底終結了傳統編譯器依賴啟發式管線（Heuristic Pipelines）進行「破壞性重寫」的黑暗時代，以嚴謹的抽象代數與圖論結構，在多項式空間內實現了對指數級乃至無窮重寫空間的無損探索。

---

#### 1. 核心理論溯源與歷史演進

1. **同餘閉包的判定過程（1980）**：
   E-graph 的數學雛形最早由圖靈獎得主 Greg Nelson 與 Derek Oppen 在其開創性論文《Fast Decision Procedures Based on Congruence Closure》（JACM 1980）中提出，作為一階邏輯可判定子集（包含無解釋函數符號的等式理論，EUF）的自動化判定過程。
2. **等價飽和的提出（POPL 2009）**：
   Ross Tate、Michael Stepp、Sorin Lerner 等人在 POPL 2009 發表奠基性論文《Equality Saturation: a new approach to optimization》，首次提出利用 E-graph 不再進行破壞性重寫，而是將所有等價表達式同時累積至「固定點飽和」，隨後全域提取最優項的構想。
3. **`egg` 庫與現代文藝復興（POPL 2021）**：
   Max Willsey 等人在 POPL 2021 發表傑出論文《egg: Fast and Extensible Equality Saturation》，引入了**延遲重建（Deferred Rebuilding / Amortized Invariant Maintenance）**機制與基於最壞情況最優聯結（Leapfrog Triejoin）的高效 E-matching，使 E-graph 的構建與飽和速度提升了數個數量級，引發了全球學術界與工業界的爆發式應用（如 Rust Cranelift、Tensat、Herbie、Glensat 等）。
4. **範疇論與圖形重寫（2025–2026）**：
   正如 Topos Institute 在 2026 最新前沿研究中所揭示的，E-graph 的本質可以被嚴格範疇化為**對稱么半範疇（Symmetric Monoidal Categories）中的圖形重寫（String Diagrammatic Rewriting）**與**初始函子（Initial Functor）**的態射擴展，將代數重寫與高階拓撲圖論深度統一起來。

---

#### 2. 形式化數學定義與代數結構

考慮一個由函數符號簽名 $\Sigma$（每個符號 $f \in \Sigma$ 具有固定元數 $\text{arity}(f)$）與變數集 $\mathcal{X}$ 生成的一階項代數（Term Algebra）$\mathcal{T}(\Sigma, \mathcal{X})$。

##### (1) 同餘關係（Congruence Relation）
給定項代數上的等價關係 $\equiv \subseteq \mathcal{T}(\Sigma) \times \mathcal{T}(\Sigma)$，若對任意 $n$ 元函數符號 $f \in \Sigma$ 以及項 $s_1, \dots, s_n$ 和 $t_1, \dots, t_n$，均滿足：
$$\forall i \in \{1, \dots, n\}, \quad s_i \equiv t_i \implies f(s_1, \dots, s_n) \equiv f(t_1, \dots, t_n)$$
則稱 $\equiv$ 是一個**同餘關係（Congruence Relation）**。
給定一組公理等式 $E = \{l_i = r_i\}$，包含 $E$ 的最小同餘關係即為由 $E$ 生成的**同餘閉包（Congruence Closure）**，記為 $\equiv_E$。

##### (2) 等價圖（E-Graph）形式化定義
一個 E-graph 是一個二元組 $G = (\mathcal{M}, \mathcal{U})$：
- **等價類（E-Class）**：由非空且互不相交的 E-node 集合組成的等價類集合。在底層透過一個**並查集（Disjoint-Set / Union-Find）**結構 $\mathcal{U}$ 維護。每個等價類擁有一個唯一的識別字 $c \in \mathcal{C}$（Class ID）。
- **等價節點（E-Node）**：一個形式為 $f(c_1, c_2, \dots, c_k)$ 的算子節點，其中 $f \in \Sigma$，而每個子節點不再是具體的項，而是指向某個等價類的識別字 $c_i \in \mathcal{C}$。
- **雜湊映射表（Hashcons / Memo）**：一個雙向映射 $\mathcal{M}: \text{e-node} \to \mathcal{C}$，保證結構全同（Structural Identity）的 E-node 永遠被規範化並映射至唯一的 E-class。

```mermaid
graph TD
    subgraph E-Class 1: c1 (Representing 2)
        n1["Constant: 2"]
    end

    subgraph E-Class 2: c2 (Representing x)
        n2["Variable: x"]
    end

    subgraph E-Class 3: c3 (Representing x * 2 and x << 1)
        n3["Operator: * (children: c2, c1)"]
        n4["Operator: << (children: c2, 1)"]
    end

    n3 -->|left child| n2
    n3 -->|right child| n1
    n4 -->|left child| n2
```

---

#### 3. 項重寫系統（TRS）之痛：階段排序問題（Phase Ordering Problem）

傳統編譯器優化（如 GCC, LLVM）本質上是一組有向重寫規則系統（Term Rewriting System, TRS）：
$$l \to r$$
這種傳統重寫面臨兩大理論瓶頸：

1. **合流性（Confluence）與終止性（Termination）的不可兼得**：
   依據項重寫經典理論（紐曼引理 Newman's Lemma），一個 TRS 具備強規範化（Strong Normalization）的充要條件是同時滿足**局部合流性**與**終止性**。然而，現實世界中的代數等價規則常常包含對稱律（$a+b \leftrightarrow b+a$）或分配律（$a(b+c) \leftrightarrow ab+ac$），這使得規則集必然包含環路，直接破壞了終止性！
2. **破壞性覆寫的貪婪局限（The Destructive Phase Ordering Trap）**：
   在傳統 AST 上，應用 $l \to r$ 意味著在記憶體中將子樹 $l$ 替換為 $r$並釋放 $l$。一旦選擇了順序：
   $$\text{Pipeline}_1: \text{Pass}_A \circ \text{Pass}_B \circ \text{Pass}_C$$
   若 $\text{Pass}_A$ 將某個子項改寫，可能徹底破壞了 $\text{Pass}_C$ 所需的前置模式匹配條件；反之，若採用：
   $$\text{Pipeline}_2: \text{Pass}_C \circ \text{Pass}_A \circ \text{Pass}_B$$
   又可能因錯失 $\text{Pass}_A$ 的常數傳播而無法觸發 $\text{Pass}_B$。
   編譯器工程師被困在排列組合 $N!$ 種 Pass 順序的無解泥沼中。

---

#### 4. 等價飽和演算法架構與核心機制

等價飽和摒棄了「破壞性替換」，轉而採用「單調增長」策略：

```text
Algorithm: Equality Saturation with E-Graphs
Input: Expression e, Rewrite Rules R, Cost Function Cost, Iteration Limit K
Output: Optimized Expression e*

1. G = EmptyEGraph()
2. root_class = G.add_expr(e)
3. loop until G is saturated (no new matches) or iteration > K:
     matches = []
     for rule (lhs -> rhs) in R:
         matches += E_MATCH(G, lhs)
     for match in matches:
         rhs_class = G.add_instantiated_expr(match.rhs)
         G.union(match.matched_class, rhs_class)
     G.rebuild()   // Crucial: Restore congruence invariants
4. e* = EXTRACT_MIN_COST(G, root_class, Cost)
5. return e*
```

##### (1) E-Matching（等價模式匹配）
在傳統樹結構中，模式匹配只需自頂向下遍歷結構。而在 E-graph 中，一個模式變數可以匹配到同一個 E-class 中的任意一個 E-node。
Willsey 等人引入了**關聯式聯結（Relational Join）**演算法（如 Leapfrog Triejoin），將 E-matching 形式化為資料庫多表查詢優化問題，在最壞情況最優複雜度下完成海量模式的並行擊發。

##### (2) 延遲重建（Deferred Rebuilding）與不變量維護
在 E-graph 中，當兩個 E-class 執行 `union(c1, c2)` 時，所有將 `c1` 或 `c2` 作為子節點的父 E-node 都會面臨「規範化失效」的問題，可能導致新的同餘關係產生。
若每次 `union` 都立即遞迴修復全圖的同餘不變量，演算法複雜度將退化至不可接受的二次方級別。
`egg` 的核心創新在於：
- 在應用規則階段，僅執行 Union-Find 的合併，暫時允許 Hashcons 處於弱不一致狀態；
- 在每輪批次重寫結束後，調用單次 `rebuild()` 函數，自底向上遍歷受影響的父節點列表（Parent Pointers），重新進行規範化與同餘去重（Hash-cons Deduplication），將同餘閉包的維護攤銷至近乎線性時間。

---

#### 5. 最優項提取策略（AST Extraction）

當 E-graph 達到等價飽和（或達到計算資源上限）後，E-graph 中緊湊地編碼了成千上萬種等價表達式。此時系統需要根據目標硬體的**代價函數（Cost Function）**提取單一最優項：

$$\text{Cost}(f(c_1, \dots, c_k)) = \text{NodeCost}(f) + \sum_{i=1}^k \text{MinCost}(c_i)$$

1. **動態規劃自底向上提取（Bottom-Up DP Extraction）**：
   在無環或有向無環圖（DAG）中，從葉節點 E-class 開始，依賴拓撲排序迭代計算每個 E-class 的最小代價及其對應的最佳 E-node。該算法時間複雜度為 $O(|G|)$，極其迅捷。
2. **0-1 整數線性規劃（Integer Linear Programming, ILP）**：
   當優化目標涉及**公共子表達式消除（Common Subexpression Elimination, CSE）**或**算子融合（Operator Fusion）**時，DAG 節點的共享會使得子樹成本不再具備簡單的代數可加性（重複計算的節點只需支付一次成本）。
   此時，將 E-graph 的提取形式化為 0-1 ILP 問題，利用 SAT/SMT 或 Gurobi/Cbc 求解器，能夠在考慮全局重疊成本的前提下求得全域精確最優解。

---

#### 6. 範疇論前沿視角：初始函子與弦圖重寫

正如 Topos Institute 在 2026 年最新論文中所闡明，等價圖與等式重寫在現代範疇論中找到了最優雅的幾何表述：

1. **對稱么半範疇（Symmetric Monoidal Category, SMC）**：
   程式中的多輸入多輸出算子（如張量運算、並發信號流）自然構成 SMC 中的態射 $f: A \otimes B \to C$。
2. **弦圖（String Diagrams）**：
   弦圖是 SMC 態射的對偶拓撲幾何表示。在弦圖中，項重寫等價於圖形的拓撲變形（2-morphisms in a 2-category）。
3. **初始函子（Initial Functors）**：
   等價飽和過程本質上是在構造自由範疇到商範疇的態射擴展。通過構造帶有商結構的圖表範疇，同餘閉包算法被精確對應於範疇圖表在推出（Pushout）與共極限（Colimit）運算下的完備化。這一理論為未來將 E-graph 拓展至高階量子電路優化與非阿貝爾群重寫奠定了堅實的數學根基。

---

### 寓言隱喻與計算機科學實體對照表

| 寓言中的奇幻元素 | 計算機科學 / 編譯器理論實體 | 形式化數學定義與工程意義 |
| :--- | :--- | :--- |
| **玄機造化司** | **編譯器中端優化框架 / 符號推導引擎** | 如 LLVM Middle-End、Rust Cranelift、MLIR、Z3 SMT Solver |
| **法儀構型樹** | **抽象語法樹（Abstract Syntax Tree, AST）** | 一階項代數 $\mathcal{T}(\Sigma, \mathcal{X})$ 中的樹狀表達式結構 |
| **九千離火銷融鼎** | **破壞性項重寫引擎（Destructive Rewriting Engine）** | 傳統編譯器中直接在記憶體中覆寫 AST 節點並釋放舊子樹的 Greedy Rewrite |
| **三昧滅形烈焰** | **破壞性就地變換（In-Place Mutation）** | $t[l \sigma] \to t[r \sigma]$，舊表達式 $l\sigma$ 永久湮滅，無法回溯 |
| **階段排序天劫** | **階段排序難題（Phase Ordering Problem）** | 不同優化 Pass 的執行順序導致互相干擾，使系統墜入局部最優陷阱 |
| **兩派工匠血戰** | **啟發式優化順序之爭（Heuristic Pipeline Design）** | 工業編譯器中為排定 Constant Folding、Inlining、DCE 等順序的繁雜經驗調優 |
| **萬象不滅之帛** | **等價圖（E-Graph, Equivalence Graph）** | $G = (\mathcal{M}, \mathcal{U})$，同時緊湊表示指數級等價項的有向圖數據結構 |
| **金色光環 / 同等之相** | **等價類（E-Class）** | 並查集中的一個不相交集合，包含所有語義完全等價的 E-node 集合 |
| **懸浮光芒節點** | **等價節點（E-Node）** | 形如 $f(c_1, \dots, c_k)$ 的算子節點，其子節點指向 E-Class ID 而非具體項 |
| **同餘法陣與共振連鎖** | **同餘閉包演算法（Congruence Closure Algorithm）** | $s_i \equiv t_i \implies f(\vec{s}) \equiv f(\vec{t})$，自動將等價關係向上傳播閉合 |
| **相印合一術** | **雜湊映射去重（Hashconsing / Structural Memoization）** | 利用 Hash Map 保證同構 E-node 永遠映射至唯一 E-Class，吸收對稱循環 |
| **圓滿飽和之境** | **等價飽和固定點（Equality Saturation Fixed Point）** | 規則庫中再無任何規則能產生新的 E-node 或觸發新的 Union 狀態 |
| **代價天秤（玉尺）** | **代價函數與提取演算法（Cost Function & AST Extraction）** | 運用動態規劃或 0-1 整數線性規劃（ILP）自底向上選取全域代價最小的 AST |
| **至簡無瑕神劍** | **全域最優代碼 / 最優計算圖** | 成功擺脫順序偏見、在全域搜索空間中提取出的極致簡化編譯產物 |

---

### 結語：在無損中見永恆

傳統的世界觀告訴我們：選擇意味著放棄，前進意味著摧毀，優化意味著在岔路口割捨無數的可能性。

然而，**等價飽和與等價圖**卻向所有計算機科學家展示了一種截然不同的優雅哲學：
真正的終極智慧，不需要急於在每一個岔路口做出非此即彼的殘酷裁決。
透過精巧的**代數共享（DAG Sharing）**與嚴謹的**同餘閉包（Congruence Closure）**，我們完全可以在有限的空間與時間之內，溫柔地包容所有的演化分支；
讓相反的規則並存，讓對稱的循環沉澱，靜待萬象交織達到圓滿飽和的彼岸。
隨後，只需一柄清醒的代價之尺，輕輕拂去塵埃，那隱藏在浩瀚宇宙中最純粹的真理，自會破曉而出。
