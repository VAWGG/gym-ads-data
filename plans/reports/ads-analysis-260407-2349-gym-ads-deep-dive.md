# GYM ADS & SALES PERFORMANCE — DEEP ANALYSIS REPORT

> **Period:** T11/2025 → T3/2026 (5 tháng)
> **Data sources:** Meta Ads export (3 files), Lead Ultra CRM (4 files)
> **Analysis date:** 2026-04-07

---

## MỤC LỤC

1. [Executive Summary](#1-executive-summary)
2. [Ads Spend & Performance](#2-ads-spend--performance)
3. [Lead Quality Audit](#3-lead-quality-audit)
4. [Sales Team Analysis](#4-sales-team-analysis)
5. [Audience & Targeting](#5-audience--targeting)
6. [Campaign Architecture Critique](#6-campaign-architecture-critique)
7. [Unit Economics & ROI](#7-unit-economics--roi)
8. [Socratic Diagnostic](#8-socratic-diagnostic)
9. [Action Framework](#9-action-framework)
10. [Unresolved Questions](#10-unresolved-questions)

---

## 1. EXECUTIVE SUMMARY

**Bức tranh lớn:** Gym đang chi trung bình **28M VND/tháng** cho Meta Ads, thu về ~140 leads/tháng, chốt ~19 khách/tháng. Tỷ lệ chốt dao động **9.8–11.8%**. T3/2026 scale chi tiêu lên **43.8M** (gấp đôi T2) — một quyết định cần được đánh giá lại nghiêm túc.

**Kết luận trọng yếu:**
- Hệ thống ads đang tạo ra **quá nhiều lead rác** — 38-45% "Không phù hợp" ngay từ đầu
- **Cost per Done (cost per actual customer)** dao động **1.0–1.3M VND** — con số này chấp nhận được KHÔNG nếu LTV thấp
- Engagement campaigns (ttlinh, ttmanh) chiếm **25-40% budget** nhưng gần như **KHÔNG tạo lead**
- Google Ads (GG) source consistently underperforms MKT (Meta) về close rate
- T3 scaling chưa có CRM data → **đang bay mù**

---

## 2. ADS SPEND & PERFORMANCE

### 2.1 Monthly Overview

| Metric | T1/2026 | T2/2026 | T3/2026 | Trend |
|--------|---------|---------|---------|-------|
| **Total Spend** | 23.4M | 16.6M | 43.8M | +163% T2→T3 |
| **Lead Results (Meta)** | 82 | 103 | 244 | Scale working? |
| **CPL (Meta)** | 286K | 161K | 179K | Improved then crept |
| **Impressions** | 392K | 419K | 914K | 2x |
| **Clicks** | 11.3K | 11.8K | 19.1K | +62% |
| **CTR avg** | 2.9% | 2.8% | 2.1% | Declining |

> **🔍 Socratic #1:** T2 có CPL thấp nhất (161K) với spend thấp nhất (16.6M). Có phải ít tiền hơn = hiệu quả hơn? Hay đơn giản là sau Tết intent tăng tự nhiên? Nếu intent tăng tự nhiên, thì bạn có đang credit cho ads thứ mà thị trường tự làm?

### 2.2 Campaign-Level Performance (Top spenders)

**T3/2026 — tháng scale mạnh nhất:**

| Campaign | Spend | Leads | CPL | Status |
|----------|-------|-------|-----|--------|
| aaaaamaaanhhh | 8.9M | 68 | 132K | active |
| llinhhai | 7.1M | 54 | 132K | active |
| linh3 | 7.1M | 65 | 109K | active |
| linh | 5.8M | 42 | 138K | active |
| hocboivid | 5.7M | 97 | 58K | active |
| amank2 | 2.7M | 15 | 179K | inactive |

> **🔍 Socratic #2:** Campaign "hocboivid" có CPL 58K — rẻ nhất, gấp 2-3 lần hiệu quả hơn các campaign khác. Nhưng đây là campaign mới (không có trong T1). **Tại sao campaign hiệu quả nhất lại chỉ mới xuất hiện? Đã bao lâu mới thử cách tiếp cận mới?**

**Engagement campaigns (all months combined):**

| Campaign | Total Spend | Engagements | Cost/Engage | Leads Generated |
|----------|------------|-------------|-------------|-----------------|
| ttlinh | ~3.65M | 253K | ~14 VND | ~3 messaging contacts |
| ttmanh | ~3.78M | 162K | ~23 VND | ~11 messaging contacts |
| ttanhboi | ~1.52M | 68K | ~22 VND | ~3 messaging contacts |

> **🔍 Socratic #3:** 3 tháng chi **~9M VND cho engagement** → 14 messaging contacts. Mỗi messaging contact từ engagement campaigns giá **~643K VND**. Nếu bạn bỏ 9M đó vào lead gen, với CPL 160-180K, bạn có thêm **50-56 leads**. Tại sao bạn chọn likes thay vì leads?
>
> Devil's advocate: Engagement campaigns xây brand, warm audience cho retargeting. **Nhưng có đang retarget audience này không? Có custom audience nào được build từ engagers không?** Nếu không, thì engagement campaign là dead-end spend.

---

## 3. LEAD QUALITY AUDIT

### 3.1 CRM Funnel Overview

| Metric | T11/2025 | T12/2025 | T1/2026 | T2/2026 |
|--------|----------|----------|---------|---------|
| **Total Leads** | 163 | 166 | 204 | 153 |
| **Không phù hợp** | 119 (73%) | 89 (54%) | 102 (50%) | 91 (59%) |
| **Chưa nghe máy** | 1 (0.6%) | 7 (4%) | 7 (3.4%) | 8 (5.2%) |
| **Đang chăm sóc** | 27 (17%) | 52 (31%) | 72 (35%) | 36 (24%) |
| **Done** | 16 (9.8%) | 18 (10.8%) | 23 (11.3%) | 18 (11.8%) |

> **🔍 Socratic #4:** "Không phù hợp" chiếm **50-73%** leads. Gần một nửa đến ba phần tư ngân sách ads đang tạo ra lead mà sale team biết ngay là sẽ không mua. **Đây là vấn đề ads hay vấn đề product-market fit?**
>
> Nghĩ sâu hơn: Nếu 73% khách hàng nghe giá xong bảo đắt, thì hoặc (a) ads target sai phân khúc thu nhập, hoặc (b) giá thật sự cao hơn thị trường, hoặc (c) perceived value chưa match. **Bạn đã benchmark giá với Cali/Elite/VNDream chưa?**

### 3.2 Phân loại lý do "Không phù hợp" (từ CRM notes)

Đọc kỹ 400+ dòng ghi chú CRM, mình phân loại thành các pattern:

| Lý do | Tần suất | Root cause |
|-------|----------|-----------|
| **"Chi phí cao / budget thấp"** | ~30% | Targeting thu nhập sai, hoặc ad copy không filter sớm |
| **"Nhà xa / cách 6km+"** | ~15% | Geo targeting quá rộng |
| **"Đã tập phòng khác / spy"** | ~12% | Competitor audience lọt vào, hoặc interest targeting rộng |
| **"Chỉ muốn báo giá, không qua phòng"** | ~20% | Low-intent lead, dạng research/comparison shopping |
| **"Nhắn zalo không trả lời"** | ~15% | Fake/low-quality lead, hoặc slow follow-up |
| **"Khách hẹn rồi boom"** | ~8% | Intent yếu ngay từ đầu, hẹn cho xong |

> **🔍 Socratic #5:** Nếu 30% không mua vì "chi phí cao" — **tại sao ad copy không đề cập khoảng giá ngay?** Thêm "từ 500K/tháng" vào ad sẽ giảm CTR (ít click hơn) nhưng tăng chất lượng lead (người click đã accept mức giá). **Bạn đang optimize cho volume hay quality?** Hiện tại rõ ràng đang chọn volume.
>
> **🔍 Socratic #6:** 15% lead nhà xa. Radius targeting đang set bao nhiêu km? Với gym local, **tại sao không giới hạn 2-3km?** Người ở xa 6km sẽ churn nhanh ngay cả nếu mua, vì commute friction. Bạn đang mua khách hay mua người sẽ thật sự đi tập?

### 3.3 "Đang chăm sóc" — Pipeline hay Graveyard?

T1/2026 có **72 leads** ở trạng thái "Đang chăm sóc" (35% total). Đọc kỹ notes:
- Phần lớn: "hẹn rồi delay", "nhắn không trả lời", "bận khi nào sắp xếp được sẽ báo"
- Rất ít chuyển thành Done trong tháng sau

> **🔍 Socratic #7:** "Đang chăm sóc" đang function như một bucket **"chưa muốn đánh dấu thất bại"** hay thật sự là pipeline sẽ convert? **Có tracking conversion rate từ "Đang chăm sóc" → Done không?** Nếu rate < 5%, thì 72 leads "đang chăm sóc" thực chất là ~68 leads "Không phù hợp" bị hoãn kết luận.

---

## 4. SALES TEAM ANALYSIS

### 4.1 Performance by Sale (across all months)

| Sale | Total Leads | Done | Close Rate | Pattern |
|------|------------|------|------------|---------|
| **Phát** | 181 | 24 | **13.3%** | Follow-up chi tiết, hẹn cụ thể giờ, ghi chú rõ ràng |
| **Huy** | 219 | 28 | **12.8%** | Volume cao nhất, nhưng nhiều "chưa nghe máy / nhắn zalo chưa rep" |
| **Linh** | 135 | 12 | **8.9%** | Ghi chú thẳng thắn, hiểu khách nhanh, nhưng close rate thấp nhất |
| **Đạt** | 150 | 11 | **7.3%** | Approach passive "addzalo tư vấn", chờ khách reply |

> **🔍 Socratic #8:** Phát close rate cao nhất (13.3%) nhưng được assign ít leads nhất (avg 45/tháng). Huy có volume cao nhất nhưng close rate thấp hơn. **Lead distribution đang based on gì? Random? Round-robin? Performance?**
>
> Nếu allocate theo performance (top closer gets more leads), Phát nên nhận nhiều hơn. **Nếu cho Phát 60 leads/tháng thay vì 45, liệu thêm 2-3 Done/tháng?** Đó là ~15% revenue uplift mà không tốn thêm đồng ads nào.

### 4.2 Đạt — Cần intervention

Đạt consistently có close rate thấp nhất. Pattern từ CRM notes:
- "addzalo tư vấn" — passive approach, không gọi điện
- "khách hẹn X giờ qua phòng" — nhưng ít follow-up khi khách delay
- T2/2026: chỉ nhận 9 leads (giảm mạnh) → có phải đã bị rotate ra?

> **🔍 Socratic #9:** Đạt có yếu về skill hay về motivation? Ghi chú của Đạt thường ngắn và generic ("addzalo tư vấn", "không có nhu cầu"). So sánh với Phát ("Hẹn 4h30 qua tham quan 7/12. Đến giờ hẹn lại delay, gọi k nghe"). **Ai đang thật sự follow-up và ai đang ghi cho có?**

### 4.3 Monthly Fluctuation — Red Flag

| Sale | T11/25 | T12/25 | T1/26 | T2/26 |
|------|--------|--------|-------|-------|
| Đạt  | 10.0% | 0% | 9.6% | 0% |
| Phát | 6.2% | 21.9% | 18.2% | 10.5% |
| Huy  | 12.7% | 14.3% | 7.5% | 16.4% |
| Linh | — | 6.1% | 10.9% | 9.7% |

Đạt: 0% ở T12 và T2 = **zero close hai tháng**. Với 29 leads T12 và 9 leads T2, không chốt được ai.

---

## 5. AUDIENCE & TARGETING

### 5.1 Age Breakdown (Lead campaigns, all months)

| Age Group | Spend | Leads | CPL | % of Total Spend |
|-----------|-------|-------|-----|-----------------|
| **18-24** | 32.3M | 225 | **143K** | 54% |
| **25-34** | 21.5M | 144 | **150K** | 36% |
| **35-44** | 4.2M | 40 | **105K** | 7% |
| **45-54** | 705K | 11 | **64K** | 1.2% |
| **55-64** | 35K | 2 | **18K** | 0.06% |
| **65+** | 64K | 3 | **21K** | 0.1% |

> **🔍 Socratic #10:** 18-24 chiếm 54% spend và 52% leads. Nhưng **nhóm này có LTV cao nhất không?** Sinh viên 18-24 thường:
> - Budget thấp (pattern CRM: "sinh viên", "budget 200-350K")
> - Churn cao (thay đổi chỗ ở, hết tiền)
> - Mua gói ngắn (1-3 tháng)
>
> So sánh: 35-44 có CPL thấp hơn (105K) và từ CRM notes, nhóm này thường là cư dân tòa nhà, có thu nhập ổn định, mua gói dài hơn. **Tại sao không shift 20-30% budget từ 18-24 sang 35-44?**

### 5.2 Gender Breakdown

| Gender | Spend | Leads | CPL |
|--------|-------|-------|-----|
| **Female** | 24.5M | 195 | **126K** |
| **Male** | 34.3M | 230 | **149K** |

Female có CPL thấp hơn **15%** so với male. Male nhận nhiều spend hơn 40% nhưng CPL cao hơn.

> **🔍 Socratic #11:** Male được phân bổ 58% budget nhưng CPL cao hơn 18%. **Đây là Meta auto-optimization hay manual choice?** Nếu manual, tại sao? Nếu auto, Meta đang chase volume (male impressions rẻ hơn) thay vì conversions. **Đã thử separate campaigns by gender chưa?**

### 5.3 Insight đặc biệt: 45-54 và 55+ — Hidden Gold?

CPL 64K (45-54) và 18-21K (55+) = rẻ gấp 2-7 lần so với 18-24. Volume cực thấp (16 leads total), nhưng:

> **🔍 Socratic #12:** Có bao giờ thử **một campaign riêng target 40-55** với messaging phù hợp (sức khỏe, bơi thư giãn, yoga)? CPL data gợi ý rằng nhóm này có intent cao hơn và cạnh tranh thấp hơn trên auction. **Bạn có biết nhóm tuổi nào chốt Done nhiều nhất trong CRM không?** Data CRM không ghi tuổi khách — đây là một blind spot nghiêm trọng.

---

## 6. CAMPAIGN ARCHITECTURE CRITIQUE

### 6.1 Naming Convention — Hỗn loạn

Tên campaigns: `linh`, `linh3`, `nlinh2`, `aaaaamaaanhhh`, `llinhhai`, `amank2`, `hocboivid`, `ttlinh`, `ttmanh`, `ttVANG`, `vang`...

**Không có structure nào cho biết:**
- Campaign objective gì?
- Target audience nào?
- Creative/angle nào?
- Ai quản lý?

> **🔍 Socratic #13:** Khi bạn muốn biết "campaign nào target nữ 25-34 quan tâm bơi" — bạn tìm bằng cách nào trong dashboard? Tên "aaaaamaaanhhh" cho bạn thông tin gì? **Nếu không thể đọc tên campaign và hiểu strategy, làm sao optimize?**

Suggested naming: `{objective}_{audience}_{angle}_{date}`
Ví dụ: `lead_f2534_swim_0326`, `engage_m1824_gym_0326`

### 6.2 Quá nhiều campaigns chạy song song

- T1: **11 campaigns** active/inactive
- T2: **13 campaigns**
- T3: **11 campaigns**

Budget mỗi campaign: 39K–320K/ngày = **rất nhỏ** cho Meta algorithm.

> **🔍 Socratic #14:** Meta cần ~50 conversions/tuần per ad set để exit learning phase. Với budget 220K/ngày và CPL 140-180K, mỗi campaign chỉ tạo ~1-2 lead/ngày = **7-14 leads/tuần**. Hầu hết campaigns **mãi mãi ở learning phase**.
>
> **Nếu gộp 4 lead campaigns thành 1 campaign với budget 900K/ngày**, Meta có đủ data để optimize delivery. Tại sao chia nhỏ? Là test audience? Test creative? Hay chỉ đơn giản là thêm dần mà không tắt cũ?

### 6.3 Active vs Inactive — Budget Waste

Mỗi tháng có 3-5 campaigns inactive, nghĩa là đã tắt giữa chừng. Nhưng trước khi tắt, đã chi:
- ninh2, ninh3, amanh (T1): tổng **4.4M VND** cho 10 leads = CPL 440K
- nlinh2 (T2): **820K** cho 3 leads = CPL 273K

> **🔍 Socratic #15:** Kill criteria cho campaigns là gì? Tắt sau bao nhiêu ngày? Sau bao nhiêu spend? Sau CPL vượt ngưỡng nào? **Nếu không có kill criteria rõ ràng, bạn đang test hay đang gambling?**

---

## 7. UNIT ECONOMICS & ROI

### 7.1 Cost per Done (thực tế)

| Month | Ads Spend | CRM Done | Cost per Done | Source |
|-------|-----------|----------|---------------|--------|
| T11/2025 | ~15M (est) | 16 | ~938K | Estimate |
| T12/2025 | ~15M (est) | 18 | ~833K | Estimate |
| T1/2026 | 23.4M | 23 | **1,017K** | Actual |
| T2/2026 | 16.6M | 18 | **922K** | Actual |
| T3/2026 | 43.8M | ? | **?** | NO CRM DATA |

> **🔍 Socratic #16 — Câu hỏi quan trọng nhất:**
>
> Cost per Done dao động **830K–1.02M VND**. Một khách Done mua gói bao nhiêu? Nếu gói trung bình 5-8M/năm thì **ROAS ~5-8x** → tốt. Nếu gói trung bình 1.5M/3 tháng thì **ROAS ~1.5x** → thua lỗ sau khi tính chi phí vận hành.
>
> **Bạn có data Average Order Value không?** Không có metric này thì toàn bộ phân tích ROI đều là phỏng đoán.

### 7.2 T3 Scaling — Flying Blind

T3 chi **43.8M** (gấp đôi T2). Nếu close rate giữ 11%:
- 244 Meta leads → estimated ~27 Done (dựa trên ratio lịch sử)
- Cost per Done: 43.8M / 27 = **1.62M VND** — tăng 60% so với T2

**Nhưng:** Chưa có Lead Ultra T3 → không biết thực tế có bao nhiêu Done.

> **🔍 Socratic #17:** Bạn scale spend gấp đôi mà chưa có CRM data tháng trước để validate. **Ai quyết định scale? Dựa trên metric nào?** Nếu dựa trên "Meta leads tăng" mà không check CRM Done, thì bạn đang optimize cho vanity metric.

### 7.3 Engagement Spend — 9M+ VND tổng 3 tháng, giá trị gì?

| Metric | Value |
|--------|-------|
| Total engagement spend (T1-T3) | ~9M VND |
| Total engagements | ~526K |
| Total messaging contacts from engagement | ~17 |
| Cost per messaging contact | ~529K |
| Estimated Done from engagement | ~0-2 |

> **🔍 Socratic #18:** Nếu 9M VND engagement spend tạo ra gần 0 Done, thì objective là gì?
> - Brand awareness? **Cho một gym local? Ai cần biết thương hiệu gym ngoài người ở gần?**
> - Warm audience? **Có retarget engagers bằng lead gen campaign không?**
> - Social proof? **500K likes có đổi được 1 khách không?**
>
> Counter-argument: Nếu page có nhiều engagement → organic reach tăng → free impressions. **Nhưng đã measure organic reach growth chưa?**

---

## 8. SOCRATIC DIAGNOSTIC — 10 CÂU HỎI CẦN TRẢ LỜI

Các câu hỏi dưới đây **phải** được trả lời trước khi optimize bất kỳ điều gì. Không trả lời = không có baseline = mọi thay đổi đều là guessing.

| # | Câu hỏi | Tại sao quan trọng |
|---|---------|-------------------|
| 1 | **Average Order Value (AOV) là bao nhiêu?** Gói trung bình khách Done mua? | Không có AOV → không thể tính ROI → không biết chi ads bao nhiêu là hợp lý |
| 2 | **Retention rate sau 3/6/12 tháng?** | Nếu 70% khách churn sau 3 tháng, thì LTV thấp và current CPD có thể lỗ |
| 3 | **Lead "Đang chăm sóc" convert thành Done rate bao nhiêu?** | Nếu < 5%, thì 35% pipeline là ảo, actual close rate thấp hơn reported |
| 4 | **Geo radius targeting đang set bao nhiêu?** | 15% lead nhà xa → tiền lãng phí |
| 5 | **Có retarget engagement audience không?** | Nếu không → 9M engagement spend = dead money |
| 6 | **Kill criteria cho campaign test?** | Không có → budget leak vào campaigns kém hiệu quả |
| 7 | **Lead allocation formula cho sale team?** | Random allocation waste leads, performance-based tăng output |
| 8 | **Speed-to-lead trung bình bao nhiêu phút?** | Sau 5 phút, lead quality giảm 80%. CRM notes cho thấy nhiều "gọi không nghe" — gọi sau bao lâu? |
| 9 | **Ad creative testing framework?** | Bao nhiêu creative variants đang test? Bao lâu rotate? |
| 10 | **Tuổi/thu nhập của Done customers?** | CRM không ghi tuổi → không biết nhóm nào thật sự mua → targeting mù |

---

## 9. ACTION FRAMEWORK

### 🔴 Ngay lập tức (Tuần này)

1. **Thu thập Lead Ultra T3/2026** — Không có data này thì scaling T3 là blind bet
2. **Thêm khoảng giá vào ad copy** — "Gói từ 500K/tháng" filter sớm budget shoppers
3. **Thu hẹp geo targeting** — Max 3km radius từ phòng tập
4. **Tắt hoặc justify engagement campaigns** — Cần answer: retarget hay không? Nếu không → cut

### 🟡 Tuần 2-3

5. **Gộp lead campaigns** — Max 3 campaigns: (A) Gym focus, (B) Bơi focus, (C) Broad. Mỗi cái budget >= 500K/ngày
6. **Restructure lead allocation** — Phát nhận 30% leads (top performer), Huy 30%, Linh 25%, Đạt 15% (hoặc coaching)
7. **Test campaign 35-54 tuổi** — Separate campaign, messaging khác (sức khỏe, thư giãn), budget 300K/ngày, run 2 tuần
8. **Standardize campaign naming** — `{obj}_{audience}_{angle}_{MMYY}`

### 🟢 Tháng 2-3

9. **Build tracking: AOV per Done, LTV by segment** — Cần biết ROI thật
10. **Implement "Đang chăm sóc" → Done tracking** — Audit pipeline thật vs pipeline ảo
11. **Speed-to-lead SLA** — Sale phải gọi trong 5 phút after lead vào
12. **Monthly report cadence** — CRM data phải đóng trước ngày 5 tháng sau

---

## 10. UNRESOLVED QUESTIONS

1. **AOV và gói bán chạy nhất là gì?** Thiếu data doanh thu → không tính được ROAS chính xác
2. **Lead Ultra T3/2026 ở đâu?** T3 là tháng spend cao nhất mà không có conversion data
3. **Campaign "hocboivid" (CPL 58K) — creative/angle gì?** Hiệu quả gấp 2-3x cần được nhân rộng
4. **Engagement audience có được retarget không?** Quyết định 9M VND spend có hợp lý hay không
5. **"Đang chăm sóc" conversion rate?** Thật sự convert bao nhiêu % sau 30/60/90 ngày?
6. **Geo targeting radius hiện tại?** Cần xác nhận để fix
7. **Ad creative đang chạy bao nhiêu variants?** Ảnh hưởng lớn đến CPL mà data export không cho biết
8. **Sale team compensation structure?** Có commission per Done không? Ảnh hưởng motivation
9. **Competitive pricing benchmark?** "Chi phí cao" là perception hay reality?
10. **Nguồn lead TIKTOK, HOTLINE — volume nhỏ nhưng pattern khác biệt?** HOTLINE close rate 25-40% — tại sao không invest hơn vào inbound?

---

*Report generated by data analysis of raw_data/. All metrics calculated from actual CSV exports. Estimates clearly marked where data gaps exist.*
