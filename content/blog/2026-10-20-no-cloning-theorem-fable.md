---
title: "研究生知識寓言：無法複製的咒文"
date: 2026-10-20T08:00:00+08:00
draft: false
tags: ["寓言", "量子資訊", "量子密碼學", "不可複製定理", "線性代數"]
categories: ["技術寓言"]
---

在遙遠的「希伯蘭王國」（Hilberan），魔法不是火球或雷暴，而是一種極其精微的力量——**咒文**。

每一道咒文都是一段純粹的波形，可用一個向量 $\lvert\psi\rangle$ 來描寫。王國中有兩種基礎波形：$\lvert 0 \rangle$（平靜如水）與 $\lvert 1 \rangle$（沸騰如火）。而真正強大的，是它們的**疊加**：

$$
\lvert\psi\rangle = \alpha\lvert 0 \rangle + \beta\lvert 1 \rangle
$$

其中 $\alpha$ 與 $\beta$ 是精確的比例，決定了一道咒文的力量與性格。王國法典的第一條，刻在魔法學院入口的石壁上，只有一行字：

> **本國的一切魔法，皆為線性。**

意思是：對兩道咒文同時施展同一種魔法，其結果等於「先分別施展、再把效果加在一起」。這句話看似平淡，卻將決定整個王國千百年以來的命運。

***

### 一、國王的心願

**希爾伯特大王**（King Hilbert）統治這片土地已逾百年。他最珍視的寶物，是一間收藏了千道珍貴咒文的圖書館。每道咒文都由 $\alpha$ 與 $\beta$ 的獨特組合決定，一旦遺失或損毀，便再也無從重現。

「如果我有一台機器，」大王對皇家工匠說，「能將任何一道咒文**原封不動地複製**一份備份，那這些無價的魔法便不會永遠消失。」

他遂下了一道聖旨：**打造一台「萬能複製機」**——只要送入一道未知咒文與一瓶「空白墨水」，機器便能產出兩份一模一樣的原件。

***

### 二、工匠的嘗試

首席工匠**狄克斯**（Dieks）領了旨。他很快發現，複製**已知**的咒文並不困難。

「大王，若我知道某道咒文是 $\lvert 0 \rangle$，我就能自無到有再塑一份 $\lvert 0 \rangle$；$\lvert 1 \rangle$ 亦然。這沒什麼了不起。」

真正的難題，出在**未知**的咒文上。

狄克斯造了一台機器，輸入槽接受兩樣東西：待複製的咒文 $\lvert\psi\rangle$，與一份空白墨水 $\lvert 0 \rangle$。機器理應輸出兩份完整的副本：

$$
\lvert\psi\rangle \otimes \lvert 0 \rangle \;\longmapsto\; \lvert\psi\rangle \otimes \lvert\psi\rangle
$$

他試了 $\lvert 0 \rangle$，成功了；試了 $\lvert 1 \rangle$，也成功了。

但當他送入疊加態 $\lvert\psi\rangle = \lvert 0 \rangle + \lvert 1 \rangle$ 時，機器吐出的卻不是

$$
(\lvert 0\rangle + \lvert 1\rangle)(\lvert 0\rangle + \lvert 1\rangle) = \lvert 00\rangle + \lvert 01\rangle + \lvert 10\rangle + \lvert 11\rangle,
$$

而是

$$
\lvert 0\rangle\lvert 0\rangle + \lvert 1\rangle\lvert 1\rangle.
$$

「……這不是副本，」狄克斯喃喃自語，「這是另一樣東西——兩份被鎖死、同生共死的糾纏，而非兩份獨立的原件。」

他意識到了什麼，卻一時說不清問題出在哪裡。

***

### 三、年輕學者的證明

一年後，一位年輕學者**沃特斯**（Wootters）走進了宮殿。

「大王，」他開口，「您要求的這台機器，在本國中**根本不可能存在**。」

「您是說，我該再花十年重造？」「不。是永遠造不出來。讓我向您說明。」

沃特斯展開一張圖：

「王國法則說，一切魔法都是**線性**的。若有一台複製機 $U$，它對任何輸入都必須滿足：

$$
U\bigl((\lvert 0\rangle + \lvert 1\rangle)\lvert 0\rangle\bigr)
= U\bigl(\lvert 0\rangle\lvert 0\rangle\bigr) + U\bigl(\lvert 1\rangle\lvert 0\rangle\bigr)
= \lvert 0\rangle\lvert 0\rangle + \lvert 1\rangle\lvert 1\rangle.
$$

這一步無可挑剔，因為線性就是這樣運作的。

但若您真的成功複製了 $\lvert 0\rangle + \lvert 1 \rangle$，正確答案應是兩份完全獨立的副本：

$$
(\lvert 0\rangle + \lvert 1\rangle)(\lvert 0\rangle + \lvert 1\rangle)
= \lvert 00\rangle + \lvert 01\rangle + \lvert 10\rangle + \lvert 11\rangle.
$$

**兩者不相等**——中間多出了 $\lvert 01\rangle + \lvert 10\rangle$ 這兩項『半真半假』的雜訊。大王，您要求的複製，本質上是一個**非線性**操作；而您的王國中，只容得下線性的魔法。您無法用線性的磚塊，砌出一堵非線性的牆。」

***

### 四、王國的真諦

大王沉默了很久。

「所以……那些珍貴的咒文，」他的聲音輕了下去，「只能有一份。永遠只有一份。」

「是的，大王。任何**未經測量**的咒文，在其原始形態下，永遠只存在一份。您不能偷偷抄錄、不能分發備份、不能複製後贈予他國。」

「那我的圖書館……」

「您只能**守護**它。或者換個思路——把真正的重要訊息『編碼』進一群看似無意義的波形之中，讓盜賊即便偷走一份，也無力還原原件。您的密碼學家會喜歡這個想法。」

***

### 五、更深層的啟示

當夜，沃特斯在日記中寫下：

「王國中的一切魔法皆為線性。而『複製一個看不見的東西』所要求的，卻是非線性——它必須**先讀出** $\lvert\psi\rangle$ 的具體內容，再依內容而動。線性操作做不了『看內容才分岔』這回事。

「再往下推一步：若真存在能複製未知咒文的機器，我便可先複製幾份、再分別測量，從而**完美讀取**任何未知態——這將徹底抹平量子世界的不確定性。但王國法則的根基，恰恰就是這份不確定性。所以，**複製未知**與**測量未知**，兩件事都做不到。

「也正因如此，在這個王國中，**秘密才是真正的秘密**——任何竊聽者，都無法完美複製你所傳輸的咒文而不留下破綻。」

***

### 揭曉

那位年輕學者論證的事，在真實世界裡叫做——

## **不可複製定理（No-Cloning Theorem）**

由 **Wootters 與 Zurek（1982）** 以及 **Dieks（1982）** 獨立提出：

> 量子力學中，不存在任何幀運算（unitary operation）$U$，使得對任意（未歸一化的）態 $\lvert\psi\rangle$，都有
> $$U\lvert\psi\rangle\lvert 0\rangle = \lvert\psi\rangle\lvert\psi\rangle.$$

核心矛盾在於：量子演算（幀運算）是**線性**的，而「完美複製一個未知態」所要求的，卻是一個**非線性**映射。二者在本質上不相容。

***

## 概念解說

### 1. 為什麼「複製已知」可行，複製未知卻不可能？

複製 $\lvert 0\rangle$ 或 $\lvert 1\rangle$ 這類**已知基態**完全可以——只需一個 CNOT 門即可：$\lvert x\rangle\lvert 0\rangle \to \lvert x\rangle\lvert x\rangle$。但對疊加態 $\lvert\psi\rangle = \alpha\lvert 0\rangle + \beta\lvert 1\rangle$，複製機必須「知道」$\alpha$、$\beta$ 的具體數值，才能輸出正確的兩份副本；而線性運算無法做到「依內容分岔」。線性只能忠實地把已知輸入的線性組合帶過去，卻保不住「張量積」的結構。

### 2. 精簡證明（反證法）

假設存在幀運算 $U$，對所有 $\lvert\psi\rangle$ 都有 $U\lvert\psi\rangle\lvert A\rangle = \lvert\psi\rangle\lvert\psi\rangle$。

- 代入 $\lvert\psi\rangle=\lvert 0\rangle$：$U\lvert 00\rangle = \lvert 00\rangle$。
- 代入 $\lvert\psi\rangle=\lvert 1\rangle$：$U\lvert 10\rangle = \lvert 11\rangle$。

取疊加態 $\lvert+\rangle = (\lvert 0\rangle + \lvert 1\rangle)/\sqrt{2}$，由**線性**得：

$$
U\lvert+\rangle\lvert A\rangle
= \frac{U\lvert 00\rangle + U\lvert 10\rangle}{\sqrt{2}}
= \frac{\lvert 00\rangle + \lvert 11\rangle}{\sqrt{2}}
= \lvert\Phi^{+}\rangle
$$

它是一個**貝爾（糾纏）態**，而非兩份獨立副本

$$
\lvert+\rangle\lvert+\rangle = \frac{1}{2}\bigl(\lvert 00\rangle + \lvert 01\rangle + \lvert 10\rangle + \lvert 11\rangle\bigr).
$$

$\lvert\Phi^{+}\rangle \neq \lvert+\rangle\lvert+\rangle$，矛盾。∎

（更一般地，對正交態 $\lvert\psi\rangle,\lvert\phi\rangle$ 取內積可得 $\langle\psi\lvert\phi\rangle = \langle\psi\lvert\phi\rangle^{\,2}$，故內積只能為 $0$ 或 $1$——即只能複製正交或相同的態，一般情形皆無解。）

### 3. 深遠影響

* **量子密碼學（QKD）**：BB84、E91（EPR）等協議的安全性，**正建立在不可複製之上**——竊聽者（Eve）無法完美複製未知量子態，任何偵聽都會在測量時留下可檢測的破綻。
* **量子計算**：無法簡單「備份」量子暫存器以容錯，因此發展出精巧的**量子誤差更正碼**（如 Shor 九碼、表面碼）繞開此限制。
* **量子資訊的哲學**：「一次一密」在量子世界是**物理法則**，而非僅為工程上的限制；未知資訊天生不可被無損拷貝。

***

## 隱喻對照表

| 故事元素 | 對應概念 |
|---|---|
| 希伯蘭王國（Hilberan） | 量子力學中的希爾伯特空間 |
| 咒文 $\lvert\psi\rangle = \alpha\lvert 0\rangle + \beta\lvert 1\rangle$ | 量子態（qubit） |
| 基礎波形 $\lvert 0\rangle$、$\lvert 1\rangle$ | 計算基態（computational basis） |
| 「一切魔法皆為線性」 | 量子力學的線性疊加原理／幀運算的線性 |
| 國王希爾伯特 | 對「備份／保護量子態」需求的提出者 |
| 大工匠狄克斯 | Dieks（1982），獨立證明了不可複製性 |
| 年輕學者沃特斯 | Wootters 與 Zurek（1982） |
| 「萬能複製機」$U\lvert\psi\rangle\lvert 0\rangle\to\lvert\psi\rangle\lvert\psi\rangle$ | 不存在的幀克隆運算（unitary cloner） |
| 疊加態複製失敗、輸出糾纏態 | 線性運算無法 preserve 張量積結構 |
| 「線性磚塊砌不出非線性的牆」 | 線性與非線性操作的本質矛盾 |
| 「秘密才是真正的秘密」 | QKD 安全性的物理基礎 |
| 「不能備份量子暫存器」 | 量子誤差更正碼出現的動機 |
| 竊聽者必留破綻 | 偵聽必然擾動量子態、提高誤碼率 |

***

**一句話總結**：王國中的一切魔法都是線性的；而「複製一個你看不見的未知之物」所要求的卻是非線性的——所以它永遠做不到；而正是這個「做不到」，讓秘密成為真正的秘密。
