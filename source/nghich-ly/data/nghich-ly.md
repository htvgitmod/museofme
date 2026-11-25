# Nghịch lý — Câu đố làm não kẹt (dữ liệu nguồn)

Tổng: **109 nghịch lý** (gom từ 5 batch, đã loại 6 mục trùng tên).
Mỗi mục: tên Anh + tên Việt, câu đố, giải thích đúng 3 câu, phân loại, link Wikipedia EN.
Tất cả 106 URL nguồn riêng biệt đã kiểm tra HTTP 200 ngày 25/11/2026; 0 mục 'chưa kiểm chứng'.

## Lưu ý nguồn
- Bootstrap / Predestination / Causal loop cùng trỏ bài Wikipedia `Temporal_paradox` (3 khái niệm khác nhau, cùng 1 bài).
- 4 nghịch lý Zeno (Achilles, Dichotomy, Arrow, Stadium) cùng trỏ bài `Zeno's paradoxes`.
- Tristram Shandy trỏ `Temporal_finitism`, Problem of future contingents trỏ `Contingency_(philosophy)`, Polchinski trỏ `Novikov_self-consistency_principle` — các bài chứa mục về nghịch lý đó, không có trang riêng.
- Inspection paradox trỏ `Renewal_theory`, Meno's paradox trỏ `Meno` (bài chứa mục).
- Paradox of choice trỏ trang sách `The_Paradox_of_Choice` của Barry Schwartz (mục này có trong List of paradoxes).
- Mpemba effect: ghi rõ trong lời giải đây là hiệu ứng quan sát, không phải nghịch lý logic thuần túy.
- 6 mục trùng đã loại khi gộp (giữ bản của batch chính A/B/D): Crocodile dilemma (E), Braess's paradox (E), Downs–Thomson paradox (E), Paradox of tolerance (E), Sleeping Beauty problem (E), Boy or Girl paradox (E).

## Danh sách

### NL-001 — Nghịch lý con tàu Theseus (Ship of Theseus) [Logic]
- Câu đố: Người Athens giữ con tàu của anh hùng Theseus làm kỷ vật, mỗi tấm ván mục được thay bằng ván mới. Sau một trăm năm, không còn tấm ván gốc nào trên tàu. Hỏi đó còn là con tàu Theseus không? Triết gia Hobbes còn thêm một xoắn nữa: giả sử có người gom hết ván cũ bị tháo ra và ráp thành một con tàu thứ hai — vậy tàu nào mới là tàu gốc?
- Lời giải: Vấn đề nằm ở chỗ ta dùng hai tiêu chí mâu thuẫn nhau: tính liên tục của hình dáng và sự giống nhau của vật liệu. Cả hai con tàu đều có lý để nhận là tàu gốc, nhưng chúng không thể đồng thời là một con tàu duy nhất. Triết học hiện đại thường giải bằng cách tách 'giống hệt' thành nhiều nghĩa khác nhau, hoặc chấp nhận rằng bản sắc qua thời gian vốn mơ hồ.
- Quiz: Theo bạn, con tàu nào là con tàu Theseus thật? — A. Tàu được sửa liên tục, dù không còn ván gốc nào; B. Tàu ráp lại từ toàn bộ ván gốc cũ; C. Cả hai đều có lý, và đó chính là nghịch lý — không có đáp án duy nhất (Đáp án: C)
- Nguồn: https://en.wikipedia.org/wiki/Ship_of_Theseus

### NL-002 — Nghịch lý kẻ nói dối (Liar paradox) [Tự tham chiếu]
- Câu đố: Xét câu này: "Câu này là sai." Nếu câu ấy đúng thì những gì nó nói là đúng, tức là nó sai. Nhưng nếu nó sai thì những gì nó nói là không đúng, tức là nó đúng. Vậy câu này đúng hay sai?
- Lời giải: Câu này tự nói về chính tính đúng sai của mình nên cả hai hướng đều dẫn tới mâu thuẫn. Tarski giải bằng cách tách ngôn ngữ thành tầng: một câu không được nói về tính đúng của chính tầng của nó. Cách khác là chấp nhận câu này không có giá trị chân lý ổn định, mà dao động giữa đúng và sai.
- Quiz: Câu "Câu này là sai" là đúng hay sai? — A. Đúng; B. Sai; C. Cả hai đáp án đều dẫn tới mâu thuẫn — đó chính là nghịch lý (Đáp án: C)
- Nguồn: https://en.wikipedia.org/wiki/Liar_paradox

### NL-003 — Nghịch lý Russell (Russell's paradox) [Tự tham chiếu]
- Câu đố: Xét tập hợp R gồm mọi tập hợp không chứa chính nó làm phần tử. Hầu hết tập hợp đều như vậy: tập hợp các con mèo không phải là một con mèo nên không chứa chính nó. Hỏi: R có chứa chính nó không? Nếu R chứa chính nó thì theo định nghĩa nó không được chứa chính nó, và ngược lại.
- Lời giải: Nếu R chứa chính nó thì theo định nghĩa nó không được chứa chính nó, và ngược lại. Mâu thuẫn này cho thấy lý thuyết tập hợp ngây thơ — cứ có tính chất là có tập hợp — là sai. Lý thuyết tập hợp hiện đại (ZFC) tránh nó bằng cách cấm các tập hợp 'quá lớn' và phân tầng các tập hợp.
- Nguồn: https://en.wikipedia.org/wiki/Russell%27s_paradox

### NL-004 — Nghịch lý thợ cạo (Barber paradox) [Tự tham chiếu]
- Câu đố: Một ngôi làng chỉ có một thợ cạo nam. Ông ta cạo cho tất cả và chỉ những người đàn ông không tự cạo râu cho mình. Hỏi: ông thợ cạo có tự cạo râu cho mình không? Nếu ông tự cạo thì ông thuộc nhóm tự cạo nên không được ông cạo, còn nếu ông không tự cạo thì ông phải được ông cạo.
- Lời giải: Nếu ông tự cạo thì ông thuộc nhóm tự cạo nên không được ông cạo, và ngược lại. Kết luận đúng là một thợ cạo như vậy không thể tồn tại — tiền đề đã tự mâu thuẫn. Đây chính là nghịch lý Russell khoác áo đời thường.
- Quiz: Ông thợ cạo có tự cạo râu cho mình không? — A. Có, ông tự cạo; B. Không, ông không tự cạo; C. Một thợ cạo như vậy không thể tồn tại (Đáp án: C)
- Nguồn: https://en.wikipedia.org/wiki/Barber_paradox

### NL-005 — Nghịch lý đống cát (Sorites paradox) [Logic]
- Câu đố: Một đống cát có 10.000 hạt. Bớt đi một hạt, nó vẫn là đống cát. Bớt thêm một hạt nữa, vẫn là đống. Cứ bớt từng hạt một như vậy, tới khi chỉ còn một hạt duy nhất. Hỏi: một hạt cát có còn là một đống cát không? Và hạt nào trong chuỗi đã biến 'đống' thành 'không phải đống'?
- Lời giải: Mỗi bước bớt một hạt dường như không đổi gì, nhưng chuỗi bước ấy dẫn từ 'đống' tới 'không phải đống'. Vấn đề nằm ở từ 'đống' vốn mơ hồ, không có ranh giới sắc nét. Các cách giải gồm logic mờ (đúng một phần), siêu định giá, hoặc chấp nhận có một hạt 'ma thuật' làm ranh giới.
- Quiz: Một hạt cát có phải là một đống cát không? — A. Phải, vì mỗi lần bớt một hạt đều không đổi gì; B. Không phải; C. Không có hạt nào là ranh giới rõ ràng — từ 'đống' vốn mơ hồ (Đáp án: C)
- Nguồn: https://en.wikipedia.org/wiki/Sorites_paradox

### NL-006 — Nghịch lý Curry (Curry's paradox) [Tự tham chiếu]
- Câu đố: Xét câu này: "Nếu câu này đúng thì ông già Noel có thật." Giả sử câu ấy đúng, thì theo chính nó, ông già Noel có thật. Mà ta vừa chứng minh được 'nếu câu này đúng thì ông già Noel có thật' — đó đúng là nội dung của câu. Vậy câu ấy đúng, và ông già Noel có thật. Bằng cùng một mẹo, ta có thể 'chứng minh' bất cứ điều gì?
- Lời giải: Chỉ cần giả sử câu đúng, ta suy ra ông già Noel có thật, rồi lại kết luận chính câu đó đúng. Vòng suy luận ấy 'chứng minh' được bất cứ điều gì, kể cả điều sai. Các nhà logic học chặn nó bằng cách hạn chế quy tắc tự suy diễn hoặc từ bỏ nguyên lý co rút trong logic.
- Nguồn: https://en.wikipedia.org/wiki/Curry%27s_paradox

### NL-007 — Nghịch lý Grelling–Nelson (Grelling–Nelson paradox) [Tự tham chiếu]
- Câu đố: Một số từ tự mô tả chính mình: từ 'ngắn' là một từ ngắn, từ 'tiếng Việt' là một từ tiếng Việt. Một số từ khác thì không: từ 'dài' không phải là một từ dài. Gọi những từ không tự mô tả mình là từ 'dị mô tả'. Hỏi: từ 'dị mô tả' có phải là một từ dị mô tả không?
- Lời giải: Nếu 'dị mô tả' là dị mô tả thì nó tự mô tả, nên nó không dị mô tả, và ngược lại. Đây là phiên bản ngôn ngữ của nghịch lý Russell, nhưng với từ ngữ thay cho tập hợp. Cách giải tương tự: tách tầng ngôn ngữ, không cho một từ nói về chính tính chất của mình ở cùng một tầng.
- Nguồn: https://en.wikipedia.org/wiki/Grelling%E2%80%93Nelson_paradox

### NL-008 — Nghịch lý Yablo (Yablo's paradox) [Tự tham chiếu]
- Câu đố: Hãy tưởng tượng một dãy vô hạn các tấm bảng. Bảng số 1 viết: 'Mọi bảng sau tôi đều sai.' Bảng số 2 cũng viết: 'Mọi bảng sau tôi đều sai.' Cứ thế mãi, không bao giờ hết. Không bảng nào tự nói về chính mình. Hỏi: có bảng nào đúng không, và dãy này có mâu thuẫn không?
- Lời giải: Dù không câu nào tự nói về chính mình, dãy vẫn mâu thuẫn: nếu một câu đúng thì câu sau nó phải vừa đúng vừa sai. Yablo cho thấy tự tham chiếu trực tiếp không phải là thủ phạm duy nhất. Tranh cãi còn mở là liệu dãy vô hạn này có ngầm chứa tự tham chiếu hay không.
- Nguồn: https://en.wikipedia.org/wiki/Yablo%27s_paradox

### NL-009 — Nghịch lý con lừa Buridan (Buridan's ass) [Logic]
- Câu đố: Một con lừa vừa đói vừa khát đứng chính giữa hai đống cỏ giống hệt nhau, cách đều nhau tới từng milimét. Mọi lý do để chọn đống bên trái đều đúng y hệt với đống bên phải. Nếu con lừa chỉ hành động khi lý trí cho nó một lý do để chọn bên này hơn bên kia, chuyện gì sẽ xảy ra với nó?
- Lời giải: Lý trí thuần túy không có cơ sở chọn bên nào, vì mọi lý do đều cân bằng nhau. Trong thực tế, con vật sẽ phá vỡ thế cân bằng nhờ một khác biệt nhỏ — đói hơn một bên, gió, hay thói quen. Nghịch lý nhắc ta rằng quyết định hợp lý đôi khi cần một yếu tố ngẫu nhiên để phá thế bế tắc.
- Quiz: Con lừa sẽ ăn đống cỏ nào? — A. Đống bên trái; B. Đống bên phải; C. Lý trí thuần túy không cho nó lý do để chọn bên nào — nó cần một yếu tố ngoài lý trí (Đáp án: C)
- Nguồn: https://en.wikipedia.org/wiki/Buridan%27s_ass

### NL-010 — Nghịch lý Burali-Forti (Burali-Forti paradox) [Logic]
- Câu đố: Số thứ tự (ordinal) là các số dùng để xếp thứ tự: thứ nhất, thứ hai, thứ ba... và còn có vô hạn số thứ tự sau các số tự nhiên. Giờ xét tập hợp gồm mọi số thứ tự. Tập hợp ấy, nếu tồn tại, tự nó phải có một số thứ tự — và số ấy phải lớn hơn mọi số thứ tự, kể cả chính nó. Điều gì sai ở đây?
- Lời giải: Tập mọi số thứ tự, nếu tồn tại, tự nó phải có một số thứ tự lớn hơn mọi số thứ tự, kể cả chính nó. Mâu thuẫn này cùng họ với nghịch lý Russell và Cantor. Lý thuyết tập hợp hiện đại kết luận: lớp các số thứ tự quá lớn để là một tập hợp.
- Nguồn: https://en.wikipedia.org/wiki/Burali-Forti_paradox

### NL-011 — Nghịch lý Cantor (Cantor's paradox) [Logic]
- Câu đố: Xét 'tập hợp của mọi tập hợp' — gọi là U. Mọi tập hợp đều là phần tử của U, kể cả tập lũy thừa của U (tập gồm mọi tập con của U). Nhưng định lý Cantor đã chứng minh tập lũy thừa của một tập hợp luôn lớn hơn chính tập hợp ấy. Vậy U vừa phải lớn hơn vừa không lớn hơn chính nó?
- Lời giải: Tập mọi tập hợp phải chứa tập lũy thừa của chính nó, mà tập lũy thừa luôn lớn hơn tập gốc theo định lý Cantor. Vậy tập đó vừa phải lớn hơn vừa không lớn hơn chính nó. Kết luận là không có 'tập hợp của mọi tập hợp'.
- Nguồn: https://en.wikipedia.org/wiki/Cantor%27s_paradox

### NL-012 — Nghịch lý Richard (Richard's paradox) [Tự tham chiếu]
- Câu đố: Hãy liệt kê mọi số thập phân có thể định nghĩa được bằng một câu tiếng Anh với số từ hữu hạn — danh sách này đếm được, nên ta đánh số chúng 1, 2, 3... Giờ dùng phương pháp đường chéo: tạo ra một số thập phân mới mà chữ số thứ n của nó khác chữ số thứ n của số thứ n trong danh sách. Số mới này khác mọi số trong danh sách, nhưng chính câu định nghĩa vừa rồi lại là một định nghĩa bằng tiếng Anh — vậy nó phải nằm trong danh sách?
- Lời giải: Bằng phương pháp đường chéo, ta định nghĩa được một số thập phân khác mọi số trong danh sách, nhưng chính định nghĩa đó lại nằm trong danh sách. Mâu thuẫn xuất phát từ việc lẫn lộn 'định nghĩa được' ở các tầng ngôn ngữ khác nhau. Richard cho thấy khái niệm 'định nghĩa được bằng tiếng Anh' cần được phân tầng chặt chẽ.
- Nguồn: https://en.wikipedia.org/wiki/Richard%27s_paradox

### NL-013 — Nghịch lý Berry (Berry paradox) [Tự tham chiếu]
- Câu đố: Xét cụm từ tiếng Anh: 'the smallest positive integer not definable in under sixty letters' — tạm dịch: 'số nguyên dương nhỏ nhất không thể định nghĩa bằng dưới sáu mươi chữ cái'. Cụm từ này có ít hơn sáu mươi chữ cái, nhưng nó vừa định nghĩa chính số mà nó bảo là không thể định nghĩa. Vậy số đó có định nghĩa được không?
- Lời giải: Cụm từ có ít hơn sáu mươi chữ cái nhưng lại đặt tên cho chính số mà nó bảo là không đặt tên được. Đây là phiên bản gọn của nghịch lý Richard, và là tổ tiên của nghịch lý Berry trong lý thuyết thông tin. Cách giải cũng là phân tầng: 'đặt tên được' phải được hiểu ở một tầng ngôn ngữ cố định.
- Nguồn: https://en.wikipedia.org/wiki/Berry_paradox

### NL-014 — Nghịch lý vụ treo cổ bất ngờ (Unexpected hanging paradox) [Logic]
- Câu đố: Một tử tù được báo: anh sẽ bị treo cổ vào một ngày trong tuần tới (thứ Hai tới thứ Sáu), và đó sẽ là một ngày bất ngờ — anh không thể biết trước vào tối hôm trước. Tử tù suy luận: nếu còn sống tới tối thứ Năm thì ngày treo chỉ có thể là thứ Sáu, vậy không còn bất ngờ, nên thứ Sáu bị loại. Rồi cứ thế loại dần thứ Năm, thứ Tư... cả tuần. Anh kết luận mình sẽ không bị treo. Nhưng rồi người ta treo anh vào thứ Tư — và anh hoàn toàn bất ngờ. Suy luận của anh sai ở đâu?
- Lời giải: Tử tù suy luận ngược từ thứ Sáu: nếu còn sống tới tối thứ Năm thì ngày treo không còn bất ngờ, nên loại thứ Sáu, rồi loại dần cả tuần. Nhưng khi người ta treo anh vào thứ Tư, anh vẫn bất ngờ thật. Mâu thuẫn nằm ở chỗ 'bất ngờ' tự hủy khi ta suy luận về chính nó, và các nhà triết học vẫn tranh cãi lỗi nằm ở bước nào.
- Quiz: Suy luận loại dần từng ngày của tử tù có đúng không? — A. Đúng — anh ta sẽ không bị treo; B. Sai ở bước đầu tiên; C. Không — anh ta vẫn bị treo vào một ngày bất ngờ thật, vì lập luận tự hủy khi áp dụng cho chính nó (Đáp án: C)
- Nguồn: https://en.wikipedia.org/wiki/Unexpected_hanging_paradox

### NL-015 — Nghịch lý con quạ (Raven paradox) [Logic]
- Câu đố: Giả thuyết 'mọi con quạ đều đen' tương đương logic với 'mọi vật không đen đều không phải quạ'. Theo quy tắc xác nhận thông thường, thấy một con quạ đen sẽ củng cố giả thuyết. Nhưng theo đó, thấy một quả táo xanh — một vật không đen và không phải quạ — cũng xác nhận 'mọi vật không đen đều không phải quạ', tức là cũng củng cố rằng mọi con quạ đều đen. Một quả táo xanh có liên quan gì tới màu của quạ đâu?
- Lời giải: Theo quy tắc xác nhận của Hempel, quả táo xanh xác nhận 'mọi vật không đen đều không phải quạ', mà mệnh đề này tương đương logic với 'mọi quạ đều đen'. Trực giác thì quả táo chẳng liên quan gì tới quạ, nên đây là nghịch lý. Cách giải thường gặp là phân biệt mức độ xác nhận: quả táo xác nhận rất ít, còn quạ đen xác nhận rất nhiều.
- Nguồn: https://en.wikipedia.org/wiki/Raven_paradox

### NL-016 — Nghịch lý xổ số (Lottery paradox) [Logic]
- Câu đố: Một kỳ xổ số có 1.000.000 vé, chỉ đúng một vé trúng. Với bất kỳ vé nào, tin rằng 'vé này không trúng' là hoàn toàn hợp lý, vì xác suất trúng chỉ là một phần triệu. Nhưng nếu ta tin như vậy về từng vé một, hợp tất cả lại thì thành 'không vé nào trúng' — trong khi chắc chắn có một vé trúng. Vậy ta có nên tin từng vé không trúng không?
- Lời giải: Tin từng vé không trúng là hợp lý, nhưng hợp các niềm tin ấy lại thì thành 'không vé nào trúng', mâu thuẫn với việc chắc chắn có vé trúng. Nghịch lý cho thấy niềm tin hợp lý không đóng kín dưới phép hợp: xác suất cao chưa đủ thành tri thức. Các cách giải đặt ngưỡng niềm tin cao hơn hoặc bỏ hẳn khái niệm 'tin' dạng nhị phân.
- Nguồn: https://en.wikipedia.org/wiki/Lottery_paradox

### NL-017 — Nghịch lý lời tựa (Preface paradox) [Logic]
- Câu đố: Một tác giả viết một cuốn sách dày 500 trang, mỗi khẳng định trong sách đều được kiểm chứng cẩn thận nên tác giả tin từng câu là đúng. Nhưng đồng thời, tác giả cũng tin chắc rằng trong một cuốn sách dày như vậy thế nào cũng sót ít nhất một lỗi — nên trong lời tựa, ông viết: 'Chắc chắn cuốn sách này còn sai sót.' Vậy tác giả vừa tin mọi câu đều đúng, vừa tin có câu sai?
- Lời giải: Tác giả có lý do tốt cho từng khẳng định riêng lẻ, và cũng có lý do tốt để tin rằng một cuốn sách dày thế nào cũng sót lỗi. Hai niềm tin ấy mâu thuẫn nhau nếu niềm tin phải đóng kín dưới phép hợp. Nghịch lý này là anh em với nghịch lý xổ số, và cùng đặt câu hỏi về tính nhất quán của niềm tin hợp lý.
- Nguồn: https://en.wikipedia.org/wiki/Preface_paradox

### NL-018 — Nghịch lý Moore (Moore's paradox) [Logic]
- Câu đố: Hãy nói to câu này: 'Trời đang mưa, nhưng tôi không tin là trời đang mưa.' Nghe rất vô lý, phải không? Nhưng câu ấy hoàn toàn có thể đúng: trời mưa thật, mà bạn lại chưa tin — chẳng hạn bạn đang ngủ trong phòng kín. Vậy vì sao một câu có thể đúng mà nói ra lại nghe vô lý đến thế?
- Lời giải: Câu này có thể đúng: trời mưa thật mà bạn chưa tin, chẳng hạn bạn đang ngủ. Nhưng chính bạn nói ra nó thì lại tự mâu thuẫn, vì nói 'trời mưa' hàm ý bạn tin trời mưa. Wittgenstein coi đây là đóng góp quan trọng nhất của Moore, và tới nay vẫn chưa có cách giải nào được mọi người đồng thuận.
- Quiz: Câu 'Trời đang mưa, nhưng tôi không tin trời đang mưa' là gì? — A. Một câu sai; B. Một câu có thể đúng, nhưng người nói không thể nói ra một cách nhất quán; C. Một câu vô nghĩa (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Moore%27s_paradox

### NL-019 — Nghịch lý Fitch về tính có thể biết (Fitch's paradox of knowability) [Logic]
- Câu đố: Giả sử mọi sự thật đều có thể biết được về nguyên tắc — chỉ cần đủ thời gian và công sức, con người sẽ biết hết. Giờ lấy một sự thật mà hiện chưa ai biết, gọi là p, ví dụ 'số hạt cát chính xác trên bãi biển này'. Nếu 'p và chưa ai biết p' có thể biết được, thì sẽ có người biết nó — nhưng biết nó thì nó không còn là 'chưa ai biết' nữa. Suy ra điều gì?
- Lời giải: Lấy một sự thật chưa ai biết, gọi là p; nếu p có thể biết được thì sẽ có người biết 'p và chưa ai biết p', điều này tự mâu thuẫn. Suy ra không thể có sự thật chưa biết nào, tức là mọi sự thật đều đã được biết — kết luận vô lý. Nghịch lý thách thức chủ nghĩa kiểm chứng, và các cách giải thường hạn chế nguyên tắc 'mọi sự thật đều có thể biết'.
- Nguồn: https://en.wikipedia.org/wiki/Fitch%27s_paradox_of_knowability

### NL-020 — Nghịch lý kẻ biết (Knower paradox) [Tự tham chiếu]
- Câu đố: Xét câu K: 'Câu này không được ai biết.' Giả sử có người biết K, thì theo nội dung của K, K không được ai biết — mâu thuẫn. Vậy ta vừa chứng minh được K không được ai biết. Nhưng chính chứng minh đó lại làm cho K được biết — vì ta vừa biết nó. Vậy K vừa được biết vừa không được biết?
- Lời giải: Nếu K được biết thì theo định nghĩa K là không được biết, nên ta chứng minh được K không được biết. Nhưng chính chứng minh đó làm cho K được biết, nên K vừa được biết vừa không được biết. Nghịch lý là họ hàng của nghịch lý kẻ nói dối, nhưng dùng khái niệm 'biết' thay vì 'đúng', và cách giải thường phân tầng các vị từ tri thức.
- Nguồn: https://en.wikipedia.org/wiki/Knower_paradox

### NL-021 — Nghịch lý Epimenides (Epimenides paradox) [Tự tham chiếu]
- Câu đố: Epimenides là một người Crete sống vào thế kỷ 6 trước Công nguyên. Ông nói: 'Mọi người Crete đều nói dối.' Nhưng chính ông cũng là người Crete. Nếu câu nói của ông là đúng thì ông — một người Crete — cũng nói dối, tức là câu nói sai. Còn nếu câu nói sai thì sao?
- Lời giải: Nếu câu nói đúng thì chính Epimenides nói dối, nên câu nói sai; nếu câu nói sai thì có người Crete nói thật, không mâu thuẫn trực tiếp. Bản này thực ra chưa phải nghịch lý chặt chẽ như nghịch lý kẻ nói dối, vì 'mọi người Crete nói dối' có thể sai chỉ nhờ một người Crete khác nói thật. Nó nổi tiếng vì là phiên bản cổ xưa nhất của nghịch lý kẻ nói dối, từ thế kỷ 6 trước Công nguyên.
- Quiz: Câu 'Mọi người Crete đều nói dối' của Epimenides có tạo ra mâu thuẫn chặt chẽ như 'Câu này là sai' không? — A. Có, hoàn toàn giống nhau; B. Không hoàn toàn — nó chỉ mâu thuẫn khi giả sử nó đúng, còn khi sai thì vẫn nhất quán; C. Không, vì Epimenides không phải người Crete (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Epimenides_paradox

### NL-022 — Nghịch lý Quine (Quine's paradox) [Tự tham chiếu]
- Câu đố: Đọc kỹ câu này: '"Tạo ra điều sai khi đặt sau chính trích dẫn của nó" tạo ra điều sai khi đặt sau chính trích dẫn của nó.' Câu này không hề dùng từ 'câu này', cũng không chỉ tay vào chính mình. Vậy mà khi ghép lại, nó vẫn đang nói về chính nó. Nó đúng hay sai?
- Lời giải: Câu này không hề dùng từ 'câu này', nhưng khi đọc kỹ, nó vẫn nói về chính nó qua trích dẫn. Nếu nó đúng thì nó sai, và nếu sai thì nó đúng, giống hệt nghịch lý kẻ nói dối. Quine dùng nó để chứng minh rằng nghịch lý có thể nảy sinh mà không cần tự tham chiếu trực tiếp hay từ chỉ định.
- Nguồn: https://en.wikipedia.org/wiki/Quine%27s_paradox

### NL-023 — Nghịch lý cá sấu (Crocodile dilemma) [Logic]
- Câu đố: Một con cá sấu bắt con của một người cha và hứa: 'Nếu ông đoán đúng ta sẽ làm gì với đứa bé, ta sẽ trả nó lại cho ông.' Người cha đoán: 'Mày sẽ không trả con tao.' Giờ cá sấu phải làm sao? Nếu nó giữ đứa bé thì cha đoán đúng, nên theo lời hứa nó phải trả; nhưng nếu nó trả thì cha đoán sai, nên nó được quyền giữ.
- Lời giải: Nếu cá sấu giữ con thì cha đoán đúng, nên theo lời hứa nó phải trả; nhưng nếu trả thì cha đoán sai, nên nó được giữ. Cả hai lựa chọn đều vi phạm lời hứa của chính nó. Nghịch lý cho thấy một số lời hứa có điều kiện tự tham chiếu là không thể thực hiện nhất quán, và cá sấu đành phải phá luật dù làm gì.
- Quiz: Cá sấu nên làm gì? — A. Giữ đứa bé; B. Trả đứa bé; C. Cả hai lựa chọn đều vi phạm lời hứa của nó (Đáp án: C)
- Nguồn: https://en.wikipedia.org/wiki/Crocodile_dilemma

### NL-024 — Nghịch lý kéo theo (Paradox of entailment) [Logic]
- Câu đố: Trong logic cổ điển, từ hai tiền đề mâu thuẫn nhau — ví dụ 'Trời đang mưa' và 'Trời không mưa' — ta có thể suy ra bất cứ kết luận nào, kể cả 'Mặt Trăng làm bằng phô mai' hay '2 + 2 = 5'. Vì sao một mâu thuẫn nhỏ về thời tiết lại 'chứng minh' được cả những chuyện không liên quan?
- Lời giải: Trong logic cổ điển, từ mâu thuẫn suy ra được mọi mệnh đề, vì không có trường hợp nào mà tiền đề đúng mà kết luận sai. Kết quả này đúng về mặt kỹ thuật nhưng trái trực giác: mưa hay không mưa chẳng liên quan gì tới Mặt Trăng. Logic paraconsistent ra đời để chặn chính hệ quả này, cho phép mâu thuẫn cục bộ mà không nổ tung toàn bộ hệ thống.
- Nguồn: https://en.wikipedia.org/wiki/Paradox_of_entailment

### NL-025 — Nghịch lý phân tích (Paradox of analysis) [Logic]
- Câu đố: Muốn phân tích khái niệm 'anh em', ta nói: 'anh em nghĩa là con trai cùng cha mẹ'. Nếu phân tích này đúng thì hai vế phải đồng nghĩa với nhau — vậy nó chẳng cho ta biết gì mới, ai biết 'anh em' là gì thì đã biết luôn phân tích ấy. Nhưng nếu phân tích nói điều mới mẻ thì nó lại sai. Vậy một phân tích khái niệm có thể vừa đúng vừa có ích không?
- Lời giải: Một phân tích khái niệm muốn đúng thì phải đồng nghĩa với khái niệm gốc, nhưng muốn có ích thì phải nói điều ta chưa biết. Hai yêu cầu này xung đột nhau: đồng nghĩa thì tầm thường, mới mẻ thì sai. Nghịch lý này của Moore đặt câu hỏi nền tảng cho cả phương pháp triết học phân tích.
- Nguồn: https://en.wikipedia.org/wiki/Paradox_of_analysis

### NL-026 — Nghịch lý Monty Hall (Monty Hall problem) [Xác suất]
- Câu đố: Bạn tham gia gameshow với 3 cánh cửa: sau 1 cửa là ô tô, sau 2 cửa còn lại là dê. Bạn chọn cửa số 1. Người dẫn chương trình, người biết rõ thứ gì sau mỗi cửa, mở cửa số 3 để lộ một con dê rồi hỏi: bạn có muốn đổi sang cửa số 2 không? Đổi hay giữ nguyên?
- Lời giải: Đổi cửa thắng với xác suất 2/3, giữ nguyên chỉ 1/3. Lúc đầu ô tô có 2/3 khả năng nằm sau hai cửa bạn không chọn, và thông tin người dẫn mở một cửa dê dồn toàn bộ 2/3 đó sang cửa còn lại. Trực giác 50–50 là sai vì hành động của người dẫn không ngẫu nhiên mà dựa trên thông tin thật.
- Mô phỏng tương tác: monty-hall
- Nguồn: https://en.wikipedia.org/wiki/Monty_Hall_problem

### NL-027 — Nghịch lý sinh nhật (Birthday problem) [Xác suất]
- Câu đố: Trong một phòng có 23 người được chọn ngẫu nhiên, xác suất có ít nhất 2 người trùng ngày sinh là bao nhiêu? Một năm có 365 ngày, vậy 23 người dường như quá ít — nhưng đáp án là hơn 50%. Với 50 người, xác suất lên tới 97%, và với 70 người gần như chắc chắn 99,9%.
- Lời giải: Với 23 người có tới 253 cặp để so sánh, chứ không phải chỉ 23 lần so với một ngày cố định. Xác suất không ai trùng giảm dần theo từng người mới, và tại 23 người nó xuống dưới 50%. Bài toán này là nền tảng của tấn công birthday trong mật mã học.
- Mô phỏng tương tác: birthday
- Nguồn: https://en.wikipedia.org/wiki/Birthday_problem

### NL-028 — Nghịch lý Simpson (Simpson's paradox) [Xác suất]
- Câu đố: Hai cách trị sỏi thận: với sỏi nhỏ, cách A khỏi 93% (81/87) còn cách B khỏi 87% (234/270); với sỏi lớn, cách A khỏi 73% (192/263) còn cách B khỏi 69% (55/80). Cách A thắng trong từng nhóm. Nhưng gộp chung lại, cách A chỉ khỏi 78% (273/350) còn cách B khỏi 83% (289/350). Vậy cách nào tốt hơn?
- Lời giải: Cách A tốt hơn trong từng nhóm, nhưng bác sĩ hay dùng A cho sỏi lớn khó chữa hơn nên nhóm A nặng hơn. Khi gộp lại, tỉ trọng nhóm khó chữa kéo trung bình của A xuống dưới B. Nghịch lý biến mất khi so sánh trong từng nhóm đồng nhất thay vì gộp thô.
- Quiz: Theo dữ liệu trên, kết luận đúng nhất là gì? — A. Cách B tốt hơn vì tỉ lệ khỏi chung cao hơn; B. Cách A tốt hơn vì thắng trong từng nhóm; C. Chưa kết luận được nếu chưa tách theo cỡ sỏi — cách A thắng trong từng nhóm đồng nhất (Đáp án: C)
- Nguồn: https://en.wikipedia.org/wiki/Simpson%27s_paradox

### NL-029 — Nghịch lý Berkson (Berkson's paradox) [Xác suất]
- Câu đố: Hai căn bệnh vốn không liên quan gì nhau trong dân số. Nhưng khi chỉ nhìn vào bệnh nhân đang nằm viện, hai bệnh này bỗng dường như tương quan nghịch: bệnh nhân mắc bệnh này lại ít mắc bệnh kia hơn. Tương tự, trong nhóm người bạn hẹn hò (ai cũng hoặc đẹp hoặc tốt tính), người đẹp dường như hay khó tính hơn. Có thật hai đặc điểm này đối nghịch nhau?
- Lời giải: Hai bệnh vốn độc lập trong dân số, nhưng mẫu bệnh viện chỉ gồm người mắc ít nhất một bệnh. Việc chỉ nhìn nhóm đã được chọn lọc tạo ra tương quan giả giữa chúng. Đây là dạng thiên lệch chọn mẫu, còn gọi là collider bias.
- Quiz: Tương quan nghịch quan sát được trong bệnh viện có thật trong dân số không? — A. Có, hai bệnh thật sự đối nghịch nhau; B. Không, đó là tương quan giả do chỉ nhìn mẫu đã chọn lọc; C. Có, vì bệnh nhân viện là mẫu đại diện cho dân số (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Berkson%27s_paradox

### NL-030 — Ngụy biện tỉ lệ nền (Base rate fallacy) [Xác suất]
- Câu đố: Một căn bệnh hiếm gặp ở 1 trên 1.000 người. Có xét nghiệm phát hiện đúng 99% người bệnh và chỉ sai 1% trên người khỏe. Bạn đi xét nghiệm và nhận kết quả dương tính. Xác suất bạn thật sự mắc bệnh là bao nhiêu — 99% hay thấp hơn nhiều?
- Lời giải: Trong 1.000 người chỉ có 1 người thật sự mắc bệnh, nhưng xét nghiệm sai khoảng 1% trên 999 người khỏe, tức gần 10 dương tính giả. Số dương tính thật (1) nhỏ hơn nhiều so với dương tính giả (khoảng 10). Vì vậy xác suất bạn thật sự mắc bệnh chỉ khoảng 1/11, không phải 99%.
- Quiz: Bạn dương tính với xét nghiệm 99% chính xác cho bệnh hiếm 1/1.000. Xác suất bạn thật sự mắc bệnh khoảng bao nhiêu? — A. Khoảng 99%; B. Khoảng 50%; C. Khoảng 9% (1 trên 11) (Đáp án: C)
- Nguồn: https://en.wikipedia.org/wiki/Base_rate_fallacy

### NL-031 — Ngụy biện của công tố viên (Prosecutor's fallacy) [Xác suất]
- Câu đố: Tại tòa, công tố viên trình bày: mẫu ADN tại hiện trường trùng với bị cáo, và xác suất một người ngẫu nhiên trùng mẫu này chỉ là 1 trên 1.000.000. Ông kết luận: vậy chỉ có 1/1.000.000 khả năng bị cáo vô tội. Lập luận này đúng hay sai?
- Lời giải: Con số 1/1.000.000 là xác suất trùng khớp nếu bị cáo vô tội, không phải xác suất vô tội khi đã trùng khớp. Muốn kết luận phải nhân thêm tỉ lệ nền, vì trong một thành phố triệu dân vẫn có thể có vài người trùng khớp. Nhầm lẫn hai xác suất có điều kiện ngược nhau này từng góp phần gây án oan.
- Quiz: Lỗi trong lập luận của công tố viên là gì? — A. Nhầm P(trùng khớp | vô tội) với P(vô tội | trùng khớp); B. Tính sai xác suất trùng khớp ADN; C. Không có lỗi, kết luận 1/1.000.000 là đúng (Đáp án: A)
- Nguồn: https://en.wikipedia.org/wiki/Prosecutor%27s_fallacy

### NL-032 — Ngụy biện của con bạc (Gambler's fallacy) [Xác suất]
- Câu đố: Bạn tung một đồng xu công bằng và nó ra mặt ngửa 10 lần liên tiếp. Lần tung thứ 11, nhiều người tin chắc mặt sấp sắp ra vì đã quá lâu chưa ra sấp, nên đặt cược lớn vào sấp. Xác suất lần tới ra sấp thật sự là bao nhiêu?
- Lời giải: Mỗi lần tung là độc lập nên xác suất sấp vẫn là 1/2, đồng xu không có trí nhớ để bù lại chuỗi ngửa. Chuỗi 10 lần ngửa hiếm nhưng đã xảy ra thì không ảnh hưởng lần tung sau. Ngược lại, nếu tin vào vận may nóng (hot hand) trong những trò có kỹ năng thì lại là chuyện khác.
- Quiz: Sau 10 lần ngửa liên tiếp, xác suất lần tung tới ra sấp là bao nhiêu? — A. Vẫn 1/2 — mỗi lần tung độc lập; B. Cao hơn 1/2 vì sấp đã lâu chưa ra; C. Thấp hơn 1/2 vì ngửa đang có đà (Đáp án: A)
- Nguồn: https://en.wikipedia.org/wiki/Gambler%27s_fallacy

### NL-033 — Nghịch lý hai phong bì (Two-envelope paradox) [Xác suất]
- Câu đố: Bạn được cho 2 phong bì giống hệt nhau, một phong bì chứa gấp đôi tiền của phong bì kia. Bạn chọn ngẫu nhiên 1 phong bì. Trước khi mở, bạn được quyền đổi lấy phong bì còn lại. Tính thử: phong bì trên tay chứa Y đồng thì phong bì kia có 50% là 2Y và 50% là Y/2, kỳ vọng là 1,25Y — vậy đổi luôn có lợi. Nhưng sau khi đổi, lập luận y hệt lại bảo nên đổi ngược lại. Vậy có nên đổi không?
- Lời giải: Phép tính 1,25Y ngầm giả định phong bì đang cầm có thể vừa là phong bì nhỏ vừa là phong bì lớn với xác suất bằng nhau ở mọi giá trị Y. Giả định đó không thể đúng với mọi Y cùng lúc vì tổng tiền phải có một phân phối xác suất cụ thể. Khi cố định phân phối tổng tiền, lợi thế đổi phong bì biến mất và hai lựa chọn có kỳ vọng bằng nhau.
- Quiz: Có nên đổi phong bì không? — A. Nên đổi, kỳ vọng tăng 25%; B. Đổi hay giữ như nhau khi tính đúng phân phối tổng tiền; C. Không nên đổi, giữ luôn tốt hơn (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Two-envelope_paradox

### NL-034 — Bài toán Người đẹp ngủ trong rừng (Sleeping Beauty problem) [Xác suất]
- Câu đố: Người đẹp được cho ngủ vào Chủ nhật, rồi các nhà nghiên cứu tung một đồng xu. Nếu ra ngửa, cô được đánh thức vào thứ Hai một lần rồi phỏng vấn. Nếu ra sấp, cô được đánh thức cả thứ Hai lẫn thứ Ba, mỗi lần đều bị xóa trí nhớ nên không biết hôm nay là thứ mấy. Mỗi lần tỉnh dậy, cô được hỏi: bạn tin đồng xu ra ngửa với xác suất bao nhiêu — 1/2 hay 1/3?
- Lời giải: Phe 1/2 cho rằng đồng xu công bằng nên niềm tin phải giữ nguyên 1/2 bất kể số lần đánh thức. Phe 1/3 cho rằng trong 3 lần tỉnh dậy có thể xảy ra, chỉ 1 lần ứng với ngửa nên đáp án là 1/3. Tranh luận vẫn mở vì hai phe dùng hai cách đếm bằng chứng khác nhau về niềm tin tự định vị.
- Quiz: Khi tỉnh dậy, Người đẹp nên tin xác suất xu ngửa là bao nhiêu? — A. 1/2 — đồng xu công bằng; B. 1/3 — chỉ 1 trong 3 lần tỉnh dậy ứng với ngửa; C. Chưa thống nhất: phe 1/2 và phe 1/3 vẫn tranh luận (Đáp án: C)
- Nguồn: https://en.wikipedia.org/wiki/Sleeping_Beauty_problem

### NL-035 — Nghịch lý Trai hay Gái (Boy or Girl paradox) [Xác suất]
- Câu đố: Một gia đình có 2 con. Bạn biết ít nhất một trong hai là con trai. Hỏi xác suất cả hai đều là con trai là bao nhiêu? Trực giác mách 1/2 vì đứa còn lại trai hay gái ngang nhau — nhưng đáp án thật là 1/3. Vì sao?
- Lời giải: Bốn trường hợp trai–trai, trai–gái, gái–trai, gái–gái đều khả dĩ như nhau trước khi biết thông tin. Biết ít nhất một trai chỉ loại trường hợp gái–gái, còn lại 3 trường hợp và chỉ 1 là hai trai. Đáp án 1/3 gây sốc vì thông tin tưởng chừng vô hại lại loại đúng một trường hợp.
- Quiz: Gia đình 2 con, biết ít nhất 1 trai. Xác suất cả 2 đều trai là bao nhiêu? — A. 1/2; B. 1/3; C. 1/4 (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Boy_or_Girl_paradox

### NL-036 — Nghịch lý hộp Bertrand (Bertrand's box paradox) [Xác suất]
- Câu đố: Có 3 hộp giống hệt nhau: hộp 1 chứa 2 đồng vàng, hộp 2 chứa 2 đồng bạc, hộp 3 chứa 1 vàng 1 bạc. Bạn chọn ngẫu nhiên 1 hộp, thò tay rút ngẫu nhiên 1 đồng ra — đó là đồng vàng. Hỏi xác suất đồng còn lại trong hộp cũng là vàng là bao nhiêu: 1/2 hay 2/3?
- Lời giải: Có 3 đồng vàng khả dĩ được rút, trong đó 2 đồng thuộc hộp 2-vàng và chỉ 1 đồng thuộc hộp 1-vàng-1-bạc. Vì vậy đồng vàng trên tay có 2/3 khả năng đến từ hộp 2-vàng. Sai lầm 1/2 đến từ việc coi hai hộp còn lại là ngang nhau dù hộp 2-vàng dễ cho ra đồng vàng gấp đôi.
- Quiz: Rút được 1 đồng vàng, xác suất đồng còn lại cũng vàng là bao nhiêu? — A. 1/2; B. 2/3; C. 1/3 (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Bertrand%27s_box_paradox

### NL-037 — Bài toán ba tù nhân (Three Prisoners problem) [Xác suất]
- Câu đố: Ba tù nhân A, B, C đều bị kết án tử hình, nhưng một người sẽ được ân xá mà không ai biết là ai. A hỏi quản giáo tên một người trong B, C sẽ bị xử. Quản giáo nói B sẽ bị xử. A mừng rỡ vì nghĩ cơ hội sống của mình tăng từ 1/3 lên 1/2. A đúng hay C mới là người nên mừng?
- Lời giải: Cơ hội của A vẫn là 1/3 vì quản giáo luôn có thể nêu tên một người sẽ bị xử dù A có được ân xá hay không. Toàn bộ thông tin mới dồn về C, người còn lại, nên cơ hội của C tăng lên 2/3. Nếu được đổi số phận với C thì A nên đổi, giống hệt bài toán Monty Hall.
- Quiz: Sau khi quản giáo nói B sẽ bị xử, cơ hội được ân xá của A và C là bao nhiêu? — A. A 1/2, C 1/2; B. A 1/3, C 2/3 — A nên đổi số phận với C; C. A 2/3, C 1/3 (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Three_Prisoners_problem

### NL-038 — Nghịch lý St. Petersburg (St. Petersburg paradox) [Quyết định]
- Câu đố: Một sòng bạc tung đồng xu cho tới khi ra ngửa. Nếu ngửa xuất hiện ở lần tung thứ n, bạn nhận 2^n đô la: lần 1 được 2 đô, lần 2 được 4 đô, lần 3 được 8 đô, cứ thế nhân đôi. Tính kỳ vọng, trò này đáng giá vô hạn đô la. Vậy bạn sẵn sàng trả bao nhiêu để chơi một ván?
- Lời giải: Kỳ vọng tiền thưởng là vô hạn vì mỗi lần tung thêm đều cộng thêm 1 đô kỳ vọng, nhưng hầu như chắc chắn bạn chỉ thắng vài đô. Bernoulli giải thích rằng người ta tối đa hóa độ thỏa dụng chứ không phải tiền, và độ thỏa dụng tăng chậm dần theo số tiền. Vì vậy một trò chơi kỳ vọng vô hạn vẫn chỉ đáng giá một khoản nhỏ.
- Quiz: Bạn nên trả bao nhiêu để chơi trò St. Petersburg một ván? — A. Vô hạn, vì kỳ vọng tiền thưởng là vô hạn; B. Một khoản nhỏ (vài đô đến vài chục đô) vì độ thỏa dụng tăng chậm; C. 0 đô vì trò này chắc chắn thua (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/St._Petersburg_paradox

### NL-039 — Nghịch lý Ellsberg (Ellsberg paradox) [Quyết định]
- Câu đố: Có một bình chứa 30 bóng đỏ và 60 bóng đen hoặc vàng với tỉ lệ không ai biết. Đa số thích cược vào bóng đỏ (xác suất biết rõ 1/3) hơn bóng đen (xác suất mơ hồ từ 0 đến 2/3), nhưng đồng thời lại thích cược đen–vàng hơn đỏ–vàng. Hai lựa chọn này mâu thuẫn nhau ra sao?
- Lời giải: Đa số thích cược vào quả đỏ có xác suất biết rõ 1/3 hơn quả đen có xác suất mơ hồ từ 0 đến 2/3. Nhưng cùng những người đó lại thích cược đen–vàng hơn đỏ–vàng, điều không một xác suất chủ quan duy nhất nào giải thích được. Nghịch lý cho thấy con người ghét sự mơ hồ, khác với ghét rủi ro đã biết.
- Quiz: Nghịch lý Ellsberg cho thấy con người ghét nhất điều gì? — A. Rủi ro đã biết xác suất; B. Sự mơ hồ — xác suất còn không biết là bao nhiêu; C. Mất tiền trong mọi trường hợp (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Ellsberg_paradox

### NL-040 — Nghịch lý Allais (Allais paradox) [Quyết định]
- Câu đố: Lựa chọn 1: A là 1 triệu đô chắc chắn, B là 89% được 1 triệu, 10% được 5 triệu, 1% trắng tay. Lựa chọn 2: C là 11% được 1 triệu, 89% trắng tay; D là 10% được 5 triệu, 90% trắng tay. Đa số chọn A ở cặp 1 và D ở cặp 2. Cặp lựa chọn này có gì mâu thuẫn?
- Lời giải: Hai cặp lựa chọn chỉ khác nhau ở một kết quả chung có xác suất 89%, theo tiên đề độc lập thì phần chung đó không được làm đổi thứ tự ưu tiên. Đa số chọn 1A và 2B, tức vừa thích chắc chắn vừa thích mạo hiểm, nên không tồn tại hàm thỏa dụng nào mô tả được cả hai lựa chọn cùng lúc. Nghịch lý phơi bày hiệu ứng chắc chắn: con người đánh giá quá cao kết quả chắc chắn so với kết quả chỉ gần chắc chắn.
- Quiz: Cặp lựa chọn 1A + 2D của đa số vi phạm điều gì? — A. Tiên đề độc lập của lý thuyết thỏa dụng kỳ vọng; B. Quy tắc tính kỳ vọng tiền thưởng; C. Luật số lớn (Đáp án: A)
- Nguồn: https://en.wikipedia.org/wiki/Allais_paradox

### NL-041 — Nghịch lý Newcomb (Newcomb's paradox) [Quyết định]
- Câu đố: Trước mặt bạn có 2 hộp. Hộp A trong suốt chứa 1.000 đô. Hộp B mờ đục: một nhà tiên tri đúng tới 99% đã bỏ 1 triệu đô vào đó nếu đoán bạn chỉ lấy hộp B, và bỏ 0 đồng nếu đoán bạn lấy cả hai hộp. Bạn được chọn chỉ lấy hộp B, hoặc lấy cả hai hộp. Bạn lấy gì?
- Lời giải: Người lấy cả hai hộp lập luận rằng tiền đã đặt sẵn nên lấy thêm 1.000 đô không bao giờ thiệt. Người chỉ lấy hộp B lập luận rằng nhà tiên tri gần như luôn đúng nên họ gần như chắc chắn nhận 1 triệu. Sau hơn 50 năm tranh luận, hai trường phái lý thuyết quyết định vẫn cho hai đáp án ngược nhau.
- Quiz: Nghịch lý Newcomb hiện có đáp án thống nhất chưa? — A. Rồi, đáp án đúng là lấy cả hai hộp; B. Rồi, đáp án đúng là chỉ lấy hộp B; C. Chưa — hai trường phái lý thuyết quyết định vẫn cho đáp án ngược nhau (Đáp án: C)
- Nguồn: https://en.wikipedia.org/wiki/Newcomb%27s_paradox

### NL-042 — Thế lưỡng nan của tù nhân (Prisoner's dilemma) [Quyết định]
- Câu đố: Hai tù nhân bị thẩm vấn riêng. Nếu cả hai im lặng, mỗi người lĩnh 1 năm. Nếu một người phản bội còn người kia im lặng, kẻ phản bội được thả còn người im lặng lĩnh 3 năm. Nếu cả hai cùng phản bội, mỗi người lĩnh 2 năm. Mỗi tù nhân nên làm gì?
- Lời giải: Với mỗi người, phản bội luôn tốt hơn bất kể người kia làm gì nên phản bội là chiến lược trội. Nhưng khi cả hai cùng phản bội, mỗi người lĩnh 2 năm thay vì 1 năm nếu cùng im lặng. Nghịch lý nằm ở chỗ lý trí cá nhân dẫn cả hai tới kết quả tập thể tồi tệ hơn.
- Quiz: Trong thế lưỡng nan của tù nhân, điều gì xảy ra khi cả hai đều hành động hợp lý cho riêng mình? — A. Cả hai cùng được thả; B. Cả hai cùng lĩnh 2 năm — tệ hơn nếu cùng hợp tác; C. Cả hai cùng lĩnh 1 năm (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Prisoner%27s_dilemma

### NL-043 — Nghịch lý Braess (Braess's paradox) [Quyết định]
- Câu đố: Mỗi sáng 4.000 tài xế lái xe đi làm mất 65 phút. Thành phố mở thêm một đường tắt miễn phí, siêu nhanh, nối hai tuyến đường chính. Ai cũng nghĩ giờ đi làm sẽ ngắn lại. Nhưng thực tế thời gian đi làm của mọi người lại tăng lên. Vì sao thêm đường lại làm mọi thứ tệ hơn?
- Lời giải: Đường mới hấp dẫn mọi tài xế ích kỷ cùng đổ vào, gây ùn tắc ở chính đoạn đường đó. Khi mỗi người tối ưu cho riêng mình, hệ thống rơi vào cân bằng Nash tồi tệ hơn trước khi có đường mới. Hiện tượng này đã được quan sát thật ở Seoul và Stuttgart.
- Quiz: Nghịch lý Braess nói gì về việc thêm đường? — A. Thêm đường luôn giảm kẹt xe; B. Thêm đường có thể làm mọi tài xế chậm hơn vì ai cũng đổ vào đường mới; C. Thêm đường không ảnh hưởng gì tới giao thông (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Braess%27s_paradox

### NL-044 — Nghịch lý Parrondo (Parrondo's paradox) [Quyết định]
- Câu đố: Trò A là trò tung xu thiên lệch, chơi riêng thì thua dần (thua 50,5% số ván). Trò B cũng là trò tung xu thiên lệch, chơi riêng cũng thua dần, với đồng xu dùng đến phụ thuộc vào số tiền hiện có chẵn hay lẻ. Nhưng nếu bạn xen kẽ hai trò thua này — ví dụ chơi AABAAB… — thì tổng tiền lại tăng lên. Hai trò thua cộng lại thành trò thắng bằng cách nào?
- Lời giải: Trò B thua khi chơi một mình vì người chơi thường rơi vào trạng thái bất lợi của nó. Xen kẽ trò A làm thay đổi phân phối trạng thái, đẩy người chơi vào đúng trạng thái mà trò B có lợi. Kết quả là hai trò thua cộng lại thành trò thắng, nhờ sự phụ thuộc giữa các ván chứ không phải phép màu.
- Quiz: Vì sao xen kẽ hai trò thua của Parrondo lại thắng? — A. Vì trò A may mắn hơn trò B; B. Vì xen kẽ thay đổi trạng thái người chơi, đẩy họ vào trạng thái có lợi của trò B; C. Vì xác suất thắng của mỗi trò thật ra trên 50% (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Parrondo%27s_paradox

### NL-045 — Nghịch lý Condorcet (Condorcet paradox) [Quyết định]
- Câu đố: Ba cử tri bầu chọn giữa A, B, C. Người 1 thích A hơn B hơn C. Người 2 thích B hơn C hơn A. Người 3 thích C hơn A hơn B. Bỏ phiếu từng cặp: đa số thích A hơn B, đa số thích B hơn C — vậy đa số hẳn thích A hơn C? Nhưng đa số lại thích C hơn A. Ý chí tập thể ở đâu?
- Lời giải: Mỗi cử tri đều có thứ tự ưu tiên nhất quán, nhưng đa số tập thể lại xoay vòng A thắng B, B thắng C, C thắng A. Không có ứng viên nào thắng mọi đối thủ nên đa số không chọn được người chiến thắng ổn định. Đây là nền tảng dẫn tới định lý bất khả của Arrow.
- Quiz: Nghịch lý Condorcet cho thấy điều gì về bỏ phiếu đa số? — A. Đa số luôn chọn được ứng viên tốt nhất; B. Sở thích tập thể có thể xoay vòng, không có người thắng ổn định; C. Chỉ cần thêm cử tri là hết xoay vòng (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Condorcet_paradox

### NL-046 — Định lý bất khả của Arrow (Arrow's impossibility theorem) [Quyết định]
- Câu đố: Liệu có tồn tại một hệ thống bầu cử xếp hạng hoàn hảo: tôn trọng ý kiến mọi người, không có ai độc tài, và cho ra thứ tự chung nhất quán? Kenneth Arrow đã chứng minh năm 1951 rằng với từ 3 phương án trở lên, không hệ thống nào thỏa mãn cùng lúc các tiêu chí công bằng tưởng chừng tối thiểu đó. Mọi hệ thống bầu cử đều phải đánh đổi điều gì đó?
- Lời giải: Arrow chứng minh rằng với từ 3 phương án trở lên, không hệ thống xếp hạng nào thỏa cùng lúc mọi tiêu chí hợp lý như không độc tài và tôn trọng nhất trí. Mọi hệ thống đều phải hy sinh ít nhất một tiêu chí tưởng chừng tối thiểu. Kết quả này đặt nền móng cho lý thuyết lựa chọn xã hội hiện đại.
- Quiz: Định lý Arrow kết luận gì? — A. Có hệ thống bầu cử hoàn hảo nếu đủ cử tri; B. Không có hệ thống xếp hạng nào thỏa mọi tiêu chí công bằng cùng lúc; C. Chỉ có bầu cử đa số là công bằng (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Arrow%27s_impossibility_theorem

### NL-047 — Nghịch lý Abilene (Abilene paradox) [Quyết định]
- Câu đố: Một buổi chiều nóng ở Coleman, Texas, cả gia đình đang ngồi chơi domino mát mẻ trên hiên. Ông bố vợ đề nghị lái xe 53 dặm tới Abilene ăn tối ở quán ăn tự phục vụ. Không ai thật sự muốn đi, nhưng ai cũng gật đầu vì tưởng người khác muốn đi. Cả nhà đi một chuyến mệt mỏi rồi về nhà mới vỡ lẽ: hóa ra chẳng ai muốn đi cả. Vì sao cả nhóm lại làm điều không ai muốn?
- Lời giải: Mỗi người im lặng vì tưởng người khác muốn đi, và sự im lặng đó lại khiến người khác càng tin rằng cả nhóm muốn đi. Cả nhóm cùng làm điều không ai thật sự muốn, rồi về nhà mới vỡ lẽ. Thuật ngữ do Jerry Harvey đặt năm 1974 và khác với groupthink ở chỗ vấn đề là quản lý sự đồng thuận, không phải xung đột.
- Quiz: Nghịch lý Abilene khác groupthink ở điểm nào? — A. Abilene là thất bại trong quản lý sự đồng thuận, còn groupthink là áp lực đồng thuận khi có xung đột; B. Abilene chỉ xảy ra trong gia đình; C. Hai khái niệm hoàn toàn giống nhau (Đáp án: A)
- Nguồn: https://en.wikipedia.org/wiki/Abilene_paradox

### NL-048 — Nghịch lý Jevons (Jevons paradox) [Quyết định]
- Câu đố: Bóng đèn LED tiết kiệm điện gấp nhiều lần bóng sợi đốt. Máy giặt, điều hòa, ô tô ngày càng hiệu quả hơn. Theo logic, tổng lượng điện và nhiên liệu tiêu thụ phải giảm mạnh. Nhưng thực tế, nhiều khi tổng tiêu thụ lại tăng lên. Hiệu quả cao hơn sao lại khiến ta dùng nhiều hơn?
- Lời giải: Đèn rẻ hơn khiến người ta lắp nhiều đèn hơn, để sáng lâu hơn và chiếu sáng cả những chỗ trước đây không chiếu. Tổng điện tiêu thụ cho chiếu sáng có thể tăng dù mỗi bóng tiết kiệm hơn. Hiệu quả làm giảm chi phí sử dụng, và chi phí rẻ hơn lại kích thích nhu cầu tăng mạnh hơn mức tiết kiệm.
- Quiz: Nghịch lý Jevons dự báo điều gì khi một tài nguyên được dùng hiệu quả hơn? — A. Tổng tiêu thụ tài nguyên đó giảm; B. Tổng tiêu thụ tài nguyên đó có thể tăng vì dùng rẻ hơn nên dùng nhiều hơn; C. Tổng tiêu thụ không đổi (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Jevons_paradox

### NL-049 — Nghịch lý tiết kiệm (Paradox of thrift) [Quyết định]
- Câu đố: Trong suy thoái, mọi gia đình đều quyết định tiết kiệm nhiều hơn: cắt ăn ngoài, hoãn mua sắm, để dành tiền phòng thân. Mỗi gia đình làm vậy đều khôn ngoan. Nhưng nếu tất cả cùng làm vậy, tổng số tiền tiết kiệm của cả nền kinh tế sẽ tăng hay giảm?
- Lời giải: Một người tiết kiệm là khôn ngoan, nhưng khi mọi người cùng cắt chi tiêu thì cầu chung sụt giảm và thu nhập của nhau cũng giảm theo. Thu nhập giảm khiến tổng số tiền tiết kiệm được rốt cuộc còn ít hơn trước. Điều đúng ở cấp cá nhân hóa ra sai ở cấp toàn thể, và đó là cốt lõi của nghịch lý.
- Quiz: Khi mọi người cùng tiết kiệm nhiều hơn trong suy thoái, tổng tiết kiệm sẽ ra sao? — A. Tăng lên vì ai cũng để dành nhiều hơn; B. Có thể giảm vì cầu sụt làm thu nhập chung giảm theo; C. Không đổi vì tiết kiệm chỉ chuyển tiền từ tay người này sang người khác (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Paradox_of_thrift

### NL-050 — Nghịch lý Downs–Thomson (Downs–Thomson paradox) [Quyết định]
- Câu đố: Một thành phố mở rộng đường cao tốc bằng cách cắt ngân sách xe buýt, hy vọng kẹt xe giảm. Nhưng sau khi đường rộng hơn, kẹt xe không những không giảm mà còn tệ hơn. Vì sao mở rộng đường lại không cứu được giao thông?
- Lời giải: Tốc độ xe hơi trong giờ cao điểm bị neo vào tốc độ của phương tiện công cộng thay thế, vì tài xế sẽ chuyển qua lại giữa hai lựa chọn. Mở rộng đường mà cắt đầu tư xe buýt làm phương án thay thế chậm đi, kéo tốc độ đường bộ xuống theo. Muốn giảm kẹt xe phải cải thiện phương tiện công cộng, không chỉ mở thêm làn đường.
- Quiz: Theo nghịch lý Downs–Thomson, tốc độ xe hơi bị quyết định bởi điều gì? — A. Số làn đường cao tốc; B. Tốc độ của phương tiện công cộng thay thế; C. Giá xăng (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Downs%E2%80%93Thomson_paradox

### NL-051 — Nghịch lý ông nội (Grandfather paradox) [Thời gian]
- Câu đố: Bạn chế được cỗ máy thời gian, quay về năm 1950 và ngăn ông nội gặp bà nội trước khi bố bạn ra đời. Nếu ông bà không gặp nhau thì bố bạn không sinh ra, và bạn cũng không bao giờ tồn tại để quay về quá khứ. Vậy ai đã ngăn ông nội gặp bà nội?
- Lời giải: Đây là dạng nghịch lý nhất quán: một hành động trong quá khứ tự xóa bỏ nguyên nhân khiến nó xảy ra. Nguyên tắc tự nhất quán Novikov cho rằng du hành thời gian chỉ cho phép những hành động vốn đã nằm trong lịch sử, nên bạn không thể thay đổi quá khứ. Một cách giải khác là giả thuyết đa vũ trụ: bạn chỉ tạo ra một nhánh thời gian mới, còn nhánh gốc vẫn nguyên vẹn.
- Quiz: Theo nguyên tắc tự nhất quán Novikov, người du hành thời gian có thể làm gì trong quá khứ? — A. Thay đổi bất cứ điều gì mình muốn; B. Chỉ làm những việc vốn đã xảy ra trong lịch sử; C. Giết ông nội rồi quay về một vũ trụ khác (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Grandfather_paradox

### NL-052 — Nghịch lý khởi nguồn (Bootstrap paradox) [Thời gian]
- Câu đố: Năm 2050, một nhà văn nổi tiếng đưa cho bạn bản thảo cuốn tiểu thuyết hay nhất thế kỷ. Bạn mang bản thảo về năm 2020, đưa cho chính nhà văn ấy khi ông còn trẻ và chưa viết gì. Ông xuất bản nó, trở nên nổi tiếng, rồi năm 2050 đưa lại bản thảo cho bạn. Vậy ai mới là tác giả thật sự của cuốn sách?
- Lời giải: Đây là nghịch lý vòng nhân quả: thông tin tồn tại mà không có điểm khởi đầu nào, vì mỗi mắt xích đều do mắt xích kia tạo ra. Nó không mâu thuẫn logic như nghịch lý ông nội, mà chỉ vi phạm trực giác rằng mọi thứ phải có nguồn gốc. Nhiều nhà vật lý xem đây là dấu hiệu cho thấy vòng nhân quả khép kín có thể tự nhất quán, dù kỳ lạ.
- Quiz: Điểm kỳ lạ nhất của nghịch lý khởi nguồn là gì? — A. Cuốn sách bị thay đổi nội dung mỗi vòng; B. Thông tin tồn tại mà không ai sáng tạo ra nó; C. Nhà văn trẻ không bao giờ đọc bản thảo (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Temporal_paradox

### NL-053 — Nghịch lý tiền định (Predestination paradox) [Thời gian]
- Câu đố: Bạn nghe tin một vụ cháy lớn sẽ thiêu rụi thư viện thành phố vào đêm nay. Bạn quay về quá khứ để tìm nguyên nhân vụ cháy, nhưng trong lúc lục lọi trong bóng tối, bạn vô tình làm đổ một cây đèn dầu và chính ngọn lửa đó gây ra vụ cháy. Bạn đi ngăn thảm họa, nhưng hóa ra chính bạn là người gây ra nó?
- Lời giải: Đây là vòng nhân quả kiểu tiền định: nỗ lực ngăn một sự kiện lại chính là nguyên nhân tạo ra sự kiện đó. Khác với nghịch lý ông nội, ở đây không có mâu thuẫn nào, vì mọi hành động đều khớp với lịch sử đã biết. Cách giải thường gặp là chấp nhận dòng thời gian cố định: người du hành không thay đổi quá khứ, mà chỉ hoàn thành nó.
- Nguồn: https://en.wikipedia.org/wiki/Temporal_paradox

### NL-054 — Vòng lặp nhân quả (Causal loop) [Thời gian]
- Câu đố: Một quả bóng bi-a lăn về phía một lỗ sâu thời gian và chui vào đó. Nó thoát ra ở quá khứ, đúng lúc để chạm nhẹ vào chính nó lúc trẻ, làm lệch quỹ đạo của nó đúng một góc vừa đủ để nó lăn vào lỗ sâu. Quả bóng đã tự thay đổi đường đi của chính mình, vậy cú chạm đầu tiên đến từ đâu?
- Lời giải: Vòng lặp nhân quả là trường hợp tổng quát của nghịch lý khởi nguồn: một sự kiện trong tương lai trở thành nguyên nhân của chính nó trong quá khứ. Thí nghiệm bóng bi-a của Polchinski cho thấy vòng lặp kiểu này có thể tự nhất quán, vì cú chạm nhẹ vừa đủ để khép kín vòng. Vấn đề còn mở là liệu mọi điều kiện ban đầu đều có một vòng lặp tự nhất quán hay không.
- Nguồn: https://en.wikipedia.org/wiki/Temporal_paradox

### NL-055 — Nghịch lý cặp song sinh (Twin paradox) [Thời gian]
- Câu đố: Hai anh em sinh đôi cùng 20 tuổi. Một người lên tàu vũ trụ bay với tốc độ bằng 80 phần trăm tốc độ ánh sáng tới một ngôi sao cách 4 năm ánh sáng rồi quay về. Khi gặp lại, người ở nhà đã 30 tuổi còn người du hành mới 26 tuổi. Nhưng người du hành cũng có quyền nói người ở nhà mới là người chuyển động, vậy tại sao chỉ một người trẻ hơn?
- Lời giải: Hai anh em không đối xứng: chỉ người du hành phải quay đầu, tức là đổi hệ quy chiếu quán tính giữa lúc đi và lúc về. Thuyết tương đối hẹp cho thấy thời gian trôi chậm hơn trên đường đi của người du hành, và hiệu ứng này đã được đo bằng đồng hồ nguyên tử trên máy bay và vệ tinh. Vì vậy đây không phải mâu thuẫn logic thật sự, mà là hệ quả phản trực giác của sự giãn nở thời gian.
- Quiz: Vì sao chỉ người du hành trẻ hơn, dù chuyển động là tương đối? — A. Vì tàu vũ trụ nặng hơn Trái Đất; B. Vì người du hành đổi hệ quy chiếu khi quay đầu, phá vỡ tính đối xứng; C. Vì đồng hồ trên tàu chạy sai (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Twin_paradox

### NL-056 — Nghịch lý Polchinski (Polchinski's paradox) [Thời gian]
- Câu đố: Một quả bóng bi-a được bắn vào một lỗ sâu, nó sẽ thoát ra ở quá khứ và đâm sầm vào chính nó lúc trẻ, hất văng bản thân trẻ ra khỏi đường vào lỗ sâu. Nếu bản thân trẻ không vào lỗ sâu thì sẽ không có quả bóng từ tương lai quay về để đâm nó. Vậy quả bóng có vào lỗ sâu hay không?
- Lời giải: Polchinski nêu tình huống này năm 1990 để thách thức nguyên tắc tự nhất quán Novikov, vì đây là phiên bản vật lý của nghịch lý ông nội. Kip Thorne và hai học trò tìm ra lời giải tự nhất quán: quả bóng tương lai chỉ chạm nhẹ, làm lệch quỹ đạo vừa đủ để nó vẫn vào lỗ sâu. Tuy nhiên chưa ai chứng minh được mọi điều kiện ban đầu đều có một lời giải tự nhất quán như vậy.
- Nguồn: https://en.wikipedia.org/wiki/Novikov_self-consistency_principle

### NL-057 — Nghịch lý Tristram Shandy (Tristram Shandy paradox) [Thời gian]
- Câu đố: Tristram Shandy sống bất tử và viết tự truyện với tốc độ rất chậm: mỗi ngày sống mất đúng 1 năm để ghi lại. Sau 2 năm viết, anh mới ghi xong 2 ngày đầu đời, và càng sống thì phần chưa viết càng dài thêm 364 ngày mỗi năm. Nếu anh sống mãi mãi, liệu anh có bao giờ viết xong tự truyện của mình không?
- Lời giải: Bertrand Russell lập luận rằng nếu Tristram sống vô hạn, mỗi ngày thứ n sẽ được viết vào năm thứ n, nên không có ngày nào mãi mãi chưa được viết. Trực giác nói anh càng ngày càng tụt lại phía sau, nhưng toán học về tập vô hạn cho thấy hai dãy vô hạn ngày và năm có thể khớp nhau một-một. Nghịch lý này vì vậy không phải mâu thuẫn, mà là minh họa cho tính chất lạ lùng của vô hạn đếm được.
- Nguồn: https://en.wikipedia.org/wiki/Temporal_finitism

### NL-058 — Nghịch lý Thần Chết (Grim Reaper paradox) [Thời gian]
- Câu đố: Lúc 12 giờ trưa, có vô hạn Thần Chết xếp hàng để giết một người. Thần thứ nhất sẽ ra tay lúc 13 giờ, thần thứ hai lúc 12 giờ 30, thần thứ ba lúc 12 giờ 15, cứ thế mỗi thần ra tay sớm hơn một nửa khoảng còn lại. Người này chắc chắn sẽ chết trước 13 giờ, nhưng không một Thần Chết nào có thể là người giết anh ta, vì luôn có một thần khác ra tay sớm hơn. Vậy ai đã giết anh ta?
- Lời giải: Nghịch lý này lấy cảm hứng từ các nghịch lý của triết gia Benardete: mỗi Thần Chết chỉ ra tay nếu chưa ai ra tay trước, nên không thần nào thỏa điều kiện. Một cách giải là cho rằng thời gian phải rời rạc chứ không liên tục, để dãy thời gian có một mốc sớm nhất. Một cách giải khác là phủ nhận khả năng tồn tại vô hạn thực sự trong thế giới vật lý.
- Quiz: Vì sao không Thần Chết nào có thể là người giết nạn nhân? — A. Vì các Thần Chết đến muộn; B. Vì với mỗi thần, luôn có một thần khác được hẹn ra tay sớm hơn; C. Vì nạn nhân trốn thoát trước 12 giờ (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Grim_Reaper_paradox

### NL-059 — Nghịch lý hải chiến ngày mai (Problem of future contingents) [Thời gian]
- Câu đố: Aristotle đặt câu hỏi: câu nói ngày mai sẽ có một trận hải chiến là đúng hay sai ngay từ hôm nay. Nếu hôm nay nó đã đúng thì trận chiến nhất định phải xảy ra, và nếu đã sai thì nó nhất định không xảy ra. Vậy mọi chuyện ngày mai đã được định sẵn từ hôm nay, và các đô đốc có bàn bạc cũng vô ích hay sao?
- Lời giải: Vấn đề nằm ở chỗ ta trượt từ tính tất yếu của suy luận sang tính tất yếu của sự việc: đúng là nếu câu nói đúng thì trận chiến sẽ xảy ra, nhưng điều đó không khiến trận chiến trở nên tất yếu. Aristotle đề xuất rằng câu nói về tương lai chưa chắc đã đúng hay sai cho tới khi sự việc xảy ra. Các nhà logic hiện đại gọi lỗi này là ngụy biện phương thức, tức nhầm lẫn phạm vi của từ tất yếu.
- Nguồn: https://en.wikipedia.org/wiki/Contingency_(philosophy)

### NL-060 — Lập luận lười biếng (Lazy argument) [Thời gian]
- Câu đố: Bạn bị ốm nặng. Nếu số phận đã định bạn sẽ khỏi thì dù có gọi bác sĩ hay không, bạn vẫn khỏi. Nếu số phận đã định bạn không khỏi thì dù có gọi bác sĩ hay không, bạn vẫn không khỏi. Vậy gọi bác sĩ để làm gì, cứ nằm chờ số phận là xong?
- Lời giải: Lập luận này, còn gọi là lập luận nhàn rỗi, xuất phát từ triết học Hy Lạp cổ và được Cicero ghi lại đầy đủ nhất. Triết gia Chrysippus phản bác rằng việc khỏi bệnh và việc gọi bác sĩ có thể cùng được định sẵn, tức là chúng đồng-định mệnh với nhau. Lỗi của lập luận là tách kết quả khỏi các bước trung gian vốn là một phần của số phận.
- Nguồn: https://en.wikipedia.org/wiki/Lazy_argument

### NL-061 — Nghịch lý McTaggart về thời gian (McTaggart's paradox) [Thời gian]
- Câu đố: McTaggart chia thời gian thành hai dãy: dãy A xếp sự kiện theo quá khứ, hiện tại, tương lai, còn dãy B chỉ xếp theo trước và sau. Ông nói thời gian thật sự cần dãy A, vì chỉ dãy A mới có sự thay đổi. Nhưng một sự kiện không thể vừa là quá khứ, vừa là hiện tại, vừa là tương lai, vậy thời gian có thật hay không?
- Lời giải: McTaggart lập luận năm 1908 rằng dãy B không có thay đổi, vì thứ tự trước sau của hai sự kiện không bao giờ đổi. Dãy A thì có thay đổi, nhưng lại gán cho mỗi sự kiện ba tính chất mâu thuẫn nhau là quá khứ, hiện tại và tương lai. Vì cả hai dãy đều không đủ nên ông kết luận thời gian là ảo tưởng, dù đa số triết gia ngày nay không đồng ý với kết luận này.
- Nguồn: https://en.wikipedia.org/wiki/The_Unreality_of_Time

### NL-062 — Nghịch lý Andromeda (Andromeda paradox) [Thời gian]
- Câu đố: Hai người đi bộ ngược chiều nhau lướt qua nhau trên phố. Theo thuyết tương đối, hiện tại của người đi về phía thiên hà Andromeda lệch khỏi hiện tại của người đi ngược lại tới khoảng 6 ngày. Với người này, hạm đội ngoài hành tinh ở Andromeda đã xuất phát, còn với người kia, quyết định xuất phát vẫn chưa được đưa ra. Vậy hạm đội đã xuất phát hay chưa?
- Lời giải: Nghịch lý này do Roger Penrose nêu ra từ lập luận Rietdijk-Putnam: mỗi quan sát viên chuyển động khác nhau có một mặt phẳng đồng thời khác nhau. Khoảng lệch 6 ngày nghe rất lớn, nhưng nó chỉ là hệ quả toán học của phép biến đổi Lorentz trên khoảng cách 2,5 triệu năm ánh sáng. Nhiều nhà vật lý cho rằng hiện tại chỉ là một quy ước của hệ quy chiếu, không phải một lát cắt có thật của vũ trụ.
- Nguồn: https://en.wikipedia.org/wiki/Andromeda_paradox

### NL-063 — Nghịch lý Achilles và con rùa (Achilles and the tortoise) [Vô cực]
- Câu đố: Achilles chạy với tốc độ 10 mét mỗi giây đua với một con rùa chạy 1 mét mỗi giây, rùa được chấp trước 100 mét. Khi Achilles chạy hết 100 mét thì rùa đã bò thêm 10 mét. Khi Achilles chạy thêm 10 mét thì rùa lại bò thêm 1 mét, cứ thế mãi. Vậy Achilles có bao giờ bắt kịp con rùa không?
- Lời giải: Zeno lập luận rằng Achilles phải hoàn thành vô hạn bước đuổi kịp, nên không bao giờ đuổi kịp rùa. Toán học hiện đại trả lời bằng chuỗi hội tụ: 100 cộng 10 cộng 1 cộng 0,1 và cứ thế cộng mãi sẽ tiến tới đúng 111,11 mét trong thời gian hữu hạn. Vì vậy Achilles bắt kịp rùa sau khoảng 11,11 giây, và vô hạn bước có thể hoàn thành trong thời gian hữu hạn.
- Quiz: Achilles bắt kịp rùa sau bao lâu trong ví dụ trên? — A. Không bao giờ, vì còn vô hạn khoảng cách; B. Sau khoảng 11,11 giây, khi tổng quãng đường hội tụ; C. Sau đúng 100 giây (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Zeno%27s_paradoxes

### NL-064 — Nghịch lý phân đôi (Dichotomy paradox) [Vô cực]
- Câu đố: Bạn muốn đi bộ hết một đoạn đường dài 100 mét. Trước hết bạn phải đi hết một nửa, tức 50 mét. Nhưng trước khi đi hết 50 mét, bạn phải đi hết 25 mét, rồi trước đó là 12,5 mét, cứ thế chia đôi mãi không dừng. Nếu có vô hạn chặng nhỏ như vậy thì làm sao bạn bước nổi bước đầu tiên?
- Lời giải: Đây là nghịch lý Zeno nổi tiếng nhất về chuyển động, được Aristotle ghi lại trong sách Vật lý. Lời giải bằng chuỗi hình học cho thấy tổng 50 cộng 25 cộng 12,5 và cứ thế mãi bằng đúng 100 mét trong thời gian hữu hạn. Vấn đề triết học còn lại là liệu không gian và thời gian có thực sự chia nhỏ vô hạn hay có một độ dài nhỏ nhất.
- Quiz: Tổng 50 + 25 + 12,5 + 6,25 + ... bằng bao nhiêu? — A. Vô hạn; B. Đúng 100; C. Không xác định được (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Zeno%27s_paradoxes

### NL-065 — Nghịch lý mũi tên bay (Arrow paradox) [Vô cực]
- Câu đố: Một mũi tên đang bay trên không. Tại bất kỳ khoảnh khắc nào, nó cũng chiếm đúng một vị trí bằng chính kích thước của nó, tức là nó đang đứng yên tại khoảnh khắc đó. Nếu mọi khoảnh khắc nó đều đứng yên thì cả chuyến bay chỉ là tổng của những lần đứng yên, vậy mũi tên có thực sự bay không?
- Lời giải: Zeno dùng nghịch lý này để cho rằng chuyển động là ảo tưởng, vì thời gian chỉ là tập hợp các khoảnh khắc đứng yên. Lời giải hiện đại cho rằng chuyển động không nằm trong một khoảnh khắc đơn lẻ, mà nằm trong quan hệ giữa vị trí và thời gian qua nhiều khoảnh khắc. Vi phân trong giải tích chính là công cụ mô tả tốc độ tức thời mà không cần mũi tên ở hai nơi cùng lúc.
- Nguồn: https://en.wikipedia.org/wiki/Zeno%27s_paradoxes

### NL-066 — Nghịch lý sân vận động (Stadium paradox) [Vô cực]
- Câu đố: Trong sân vận động có 3 hàng xe ngựa, mỗi hàng 3 chiếc. Hàng B đứng yên, hàng A và hàng C chạy ngược chiều nhau với cùng tốc độ. Trong cùng một khoảng thời gian, hàng A vượt qua hàng B được 3 chiếc, nhưng vượt qua hàng C được 6 chiếc. Vậy cùng một khoảng thời gian lại vừa bằng một nửa, vừa bằng cả khoảng thời gian hay sao?
- Lời giải: Zeno dùng nghịch lý sân vận động, còn gọi là nghịch lý hàng chuyển động, để cho rằng thời gian có thể vừa bị halving vừa bị doubling cùng lúc. Lỗi nằm ở chỗ Zeno so sánh tốc độ tương đối với tốc độ tuyệt đối như thể chúng đo cùng một thứ. Khi phân biệt rõ vận tốc của A so với B và vận tốc của A so với C thì mâu thuẫn biến mất.
- Nguồn: https://en.wikipedia.org/wiki/Zeno%27s_paradoxes

### NL-067 — Khách sạn vô cực Hilbert (Hilbert's paradox of the Grand Hotel) [Vô cực]
- Câu đố: Khách sạn Hilbert có vô hạn phòng, đánh số 1, 2, 3 và cứ thế mãi, tất cả đều đã kín khách. Một vị khách mới đến xin phòng, lễ tân bảo vẫn còn chỗ. Rồi một đoàn xe buýt vô hạn, mỗi xe chở vô hạn khách, cùng đến xin phòng, lễ tân vẫn bảo còn chỗ. Làm sao một khách sạn đã đầy lại chứa thêm được vô hạn người?
- Lời giải: Với một khách mới, chỉ cần chuyển khách phòng n sang phòng n cộng 1 là phòng 1 trống ra, vì khách sạn vô hạn không có phòng cuối cùng. Với vô hạn khách mới, chuyển khách phòng n sang phòng 2n sẽ để trống toàn bộ phòng lẻ. Nghịch lý này cho thấy tập vô hạn đếm được có thể khớp một-một với một phần thật sự của chính nó, điều không bao giờ xảy ra với tập hữu hạn.
- Quiz: Để đón vô hạn khách mới, lễ tân chuyển khách phòng n sang phòng nào? — A. Phòng n + 1; B. Phòng 2n, để trống mọi phòng lẻ; C. Phòng n + 100 (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Hilbert's_paradox_of_the_Grand_Hotel

### NL-068 — Nghịch lý đèn Thomson (Thomson's lamp) [Vô cực]
- Câu đố: Một chiếc đèn có công tắc bật tắt. Bạn bật đèn, sau 1 phút thì tắt, sau nửa phút thì bật, sau một phần tư phút thì tắt, cứ thế mỗi lần chờ bằng một nửa lần trước. Tổng thời gian chỉ là 2 phút, nhưng bạn đã bật tắt vô hạn lần. Hết đúng 2 phút thì đèn đang bật hay đang tắt?
- Lời giải: Triết gia Thomson nêu thí nghiệm này năm 1954 để phản đối khả năng của siêu nhiệm vụ, tức hoàn thành vô hạn việc trong thời gian hữu hạn. Ông lập luận rằng đèn không thể bật, vì lần bật nào cũng bị tắt ngay sau đó, và cũng không thể tắt, vì lần tắt nào cũng bị bật ngay sau đó. Paul Benacerraf phản bác rằng trạng thái trước phút thứ 2 không quyết định trạng thái tại phút thứ 2, vì mô tả thí nghiệm còn thiếu thông tin.
- Quiz: Theo Benacerraf, vì sao câu hỏi đèn bật hay tắt ở phút thứ 2 là chưa đủ dữ kiện? — A. Vì đèn bị hỏng trước phút thứ 2; B. Vì trạng thái trước đó không quyết định trạng thái tại đúng mốc giới hạn; C. Vì công tắc chạy nhanh hơn tốc độ ánh sáng (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Thomson%27s_lamp

### NL-069 — Nghịch lý Ross–Littlewood (Ross–Littlewood paradox) [Vô cực]
- Câu đố: Một chiếc bình rỗng và vô hạn quả bóng đánh số 1, 2, 3 và cứ thế mãi. Lúc 11 giờ 59, bạn bỏ bóng 1 tới 10 vào bình rồi lấy bóng 1 ra. Sau 30 giây, bạn bỏ bóng 11 tới 20 vào rồi lấy bóng 2 ra, cứ thế mỗi bước nhanh gấp đôi bước trước để xong trước 12 giờ. Đến 12 giờ, trong bình còn bao nhiêu quả bóng?
- Lời giải: Lập luận thứ nhất nói bình phải có vô hạn bóng, vì mỗi bước thêm ròng 9 quả và số bóng chỉ tăng lên. Lập luận thứ hai nói bình phải rỗng, vì quả bóng số n nào cũng bị lấy ra ở bước n, nên không quả nào còn lại. Hai lập luận đều đúng theo cách riêng của chúng, và mâu thuẫn cho thấy giới hạn của dãy tập hợp không được quyết định bởi số lượng từng bước.
- Quiz: Theo lập luận quả bóng nào cũng bị lấy ra, đến 12 giờ bình còn mấy quả? — A. Vô hạn quả; B. 0 quả; C. 9 quả (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Ross%E2%80%93Littlewood_paradox

### NL-070 — Nghịch lý kèn Gabriel (Gabriel's horn) [Vô cực]
- Câu đố: Lấy đường cong y bằng 1 chia x với x từ 1 trở đi, xoay quanh trục x để tạo thành một chiếc kèn dài vô hạn. Chiếc kèn này có thể tích đúng bằng số pi, tức chỉ chứa được khoảng 3,14 đơn vị sơn. Nhưng diện tích mặt trong của nó lại là vô hạn, tức cần vô hạn sơn mới quét kín được. Vậy đổ sơn vào trong thì đầy, mà quét sơn lên mặt thì không bao giờ đủ?
- Lời giải: Evangelista Torricelli phát hiện ra hình này vào thế kỷ 17, và nó còn được gọi là nghịch lý người thợ sơn. Thể tích hội tụ vì nó tỉ lệ với 1 chia x bình phương, còn diện tích phân kỳ vì nó tỉ lệ với 1 chia x. Lời giải là lớp sơn sẽ mỏng dần vô hạn khi đi sâu vào kèn, nên cùng một lượng sơn vừa đủ để lấp đầy thể tích lại vừa đủ để phủ kín mặt trong nếu cho phép nó mỏng dần.
- Quiz: Thể tích của kèn Gabriel bằng bao nhiêu? — A. Vô hạn; B. Đúng bằng số pi; C. Bằng 1 (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Gabriel%27s_Horn

### NL-071 — Nghịch lý Banach–Tarski (Banach–Tarski paradox) [Vô cực]
- Câu đố: Bạn có một quả bóng đặc bằng vàng. Bạn cắt nó thành đúng 5 mảnh, rồi chỉ xoay và dịch chuyển các mảnh, không kéo giãn hay thêm vật liệu. Khi ghép lại, bạn được 2 quả bóng vàng giống hệt quả ban đầu, mỗi quả to bằng quả gốc. Bạn có thể nhân đôi vàng từ hư không hay sao?
- Lời giải: Banach và Tarski chứng minh định lý này năm 1924, dựa trên tiên đề chọn và các tập hợp không đo được. Các mảnh không phải là miếng vật chất bình thường, mà là tập hợp vô hạn điểm rải rác phức tạp tới mức không có thể tích xác định. Vì vậy định lý đúng trong toán học, nhưng không thể thực hiện trong thế giới vật lý, nơi mọi mảnh đều có thể tích.
- Nguồn: https://en.wikipedia.org/wiki/Banach%E2%80%93Tarski_paradox

### NL-072 — Siêu nhiệm vụ (Supertask) [Vô cực]
- Câu đố: Bạn phải làm vô hạn việc trong đúng 1 phút: việc thứ nhất mất nửa phút, việc thứ hai mất một phần tư phút, việc thứ ba mất một phần tám phút, cứ thế mỗi việc nhanh gấp đôi việc trước. Sau 1 phút, bạn đã làm xong vô hạn việc. Liệu một người có thể hoàn thành vô hạn việc trong thời gian hữu hạn hay không?
- Lời giải: Khái niệm siêu nhiệm vụ do triết gia Thomson đặt tên, bắt nguồn từ các nghịch lý Zeno về chuyển động. Về mặt toán học, tổng nửa cộng một phần tư cộng một phần tám và cứ thế mãi bằng đúng 1, nên vô hạn việc khớp vừa trong 1 phút. Về mặt vật lý, mỗi việc ngày càng nhanh sẽ sớm vượt mọi giới hạn tốc độ và năng lượng, nên siêu nhiệm vụ có thể khả thi về logic mà bất khả thi về vật lý.
- Nguồn: https://en.wikipedia.org/wiki/Supertask

### NL-073 — Nghịch lý hồi quy vô hạn (Infinite regress) [Vô cực]
- Câu đố: Bạn hỏi vì sao mình tin một điều gì đó, và đưa ra một lý do. Nhưng lý do đó cũng cần một lý do khác để đứng vững, và lý do khác đó lại cần một lý do nữa, cứ thế mãi không dừng. Nếu mọi niềm tin đều cần một niềm tin khác chống lưng thì làm sao có niềm tin đầu tiên nào đứng vững được?
- Lời giải: Hồi quy vô hạn là chuỗi mà mỗi mắt xích đều phụ thuộc vào mắt xích trước nó, không có điểm bắt đầu. Trong triết học, nó được dùng để phản bác các lý thuyết không có nền tảng, như ví dụ con gà và quả trứng. Các cách thoát gồm chủ nghĩa nền tảng, tức chấp nhận một số niềm tin không cần chứng minh, và chủ nghĩa vô hạn, tức chấp nhận chuỗi cứ kéo dài mãi.
- Nguồn: https://en.wikipedia.org/wiki/Infinite_regress

### NL-074 — Nghịch lý Galileo (Galileo's paradox) [Vô cực]
- Câu đố: Hầu hết các số tự nhiên đều không phải là số chính phương: trong 100 số đầu tiên chỉ có 10 số chính phương là 1, 4, 9 và cứ thế tới 100. Vậy rõ ràng số tự nhiên phải nhiều hơn số chính phương rất nhiều. Nhưng mỗi số tự nhiên n đều có đúng một số chính phương là n bình phương, và ngược lại, vậy hai tập hợp này lại bằng nhau?
- Lời giải: Galileo nêu nghịch lý này trong cuốn Hai khoa học mới năm 1638, và kết luận rằng các khái niệm ít hơn, bằng nhau và nhiều hơn chỉ áp dụng cho tập hữu hạn. Cantor sau đó xây dựng lý thuyết tập hợp cho thấy hai tập hợp vô hạn có thể khớp nhau một-một dù một tập là phần thật sự của tập kia. Đây là định nghĩa hiện đại của tập vô hạn: một tập bằng kích thước với một phần thật sự của chính nó.
- Quiz: Trong 100 số tự nhiên đầu tiên có bao nhiêu số chính phương? — A. 100 số; B. 10 số; C. 50 số (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Galileo%27s_paradox

### NL-075 — Nghịch lý chuỗi Grandi (Grandi's series) [Vô cực]
- Câu đố: Tính tổng vô hạn 1 trừ 1 cộng 1 trừ 1 và cứ thế mãi. Nếu nhóm thành từng cặp (1 trừ 1) cộng (1 trừ 1) thì tổng bằng 0. Nếu giữ lại số 1 đầu rồi nhóm 1 cộng (trừ 1 cộng 1) thì tổng bằng 1. Vậy cùng một tổng lại vừa bằng 0, vừa bằng 1 hay sao?
- Lời giải: Guido Grandi nghiên cứu chuỗi này năm 1703 và cho rằng nó bằng một phần hai, vì trung bình của 0 và 1 là một phần hai. Toán học hiện đại khẳng định chuỗi này phân kỳ, tức không có tổng theo nghĩa thông thường, vì dãy tổng riêng cứ dao động giữa 0 và 1. Các phương pháp tổng Cesàro và Abel gán cho nó giá trị một phần hai, nhưng đó là giá trị mở rộng chứ không phải tổng cổ điển.
- Quiz: Theo nghĩa tổng cổ điển, chuỗi 1 - 1 + 1 - 1 + ... có tổng bằng bao nhiêu? — A. 0; B. 1; C. Không có tổng, vì dãy tổng riêng dao động mãi (Đáp án: C)
- Nguồn: https://en.wikipedia.org/wiki/Grandi%27s_series

### NL-076 — Nghịch lý Fermi (Fermi paradox) [Vật lý]
- Câu đố: Vũ trụ có hàng tỉ ngôi sao và vô số hành tinh, nhiều hành tinh đã tồn tại lâu hơn Trái Đất rất nhiều. Nếu sự sống thông minh là chuyện thường gặp, lẽ ra các nền văn minh đã lan khắp thiên hà từ lâu và để lại dấu vết rõ ràng. Vậy mà chúng ta chưa thấy bằng chứng thuyết phục nào — vậy, mọi người ở đâu?
- Lời giải: Nghịch lý nằm ở chỗ hai tiền đề đều có vẻ đúng mà kết luận lại mâu thuẫn: vũ trụ vừa rộng lớn vừa già cỗi, nhưng lại im lặng một cách khó hiểu. Các lời giải thường tấn công một tiền đề: có thể sự sống thông minh cực hiếm, các nền văn minh tự hủy trước khi vươn xa, hoặc họ đang ở đó mà ta chưa biết cách lắng nghe. Đến nay chưa có lời giải nào được đồng thuận, nên đây vẫn là câu hỏi mở của thiên văn học.
- Quiz: Theo bạn, lời giải nào cho nghịch lý Fermi được nhiều nhà khoa học nhắc tới nhất? — A. Người ngoài hành tinh chắc chắn không tồn tại; B. Sự sống thông minh có thể cực kỳ hiếm, hoặc các nền văn minh không tồn tại đủ lâu để gặp nhau; C. Trái Đất là hành tinh duy nhất có thể có sự sống (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Fermi_paradox

### NL-077 — Con mèo của Schrödinger (Schrödinger's cat) [Vật lý]
- Câu đố: Một con mèo bị nhốt trong hộp kín cùng một cơ chế lượng tử: một hạt có thể phân rã hoặc không, và nếu phân rã thì chất độc sẽ thoát ra. Theo cơ học lượng tử, trước khi mở hộp, hạt ở trạng thái chồng chập vừa phân rã vừa chưa phân rã. Vậy con mèo trong hộp đang sống hay đã chết — hay vừa sống vừa chết?
- Lời giải: Thí nghiệm tưởng tượng này cho thấy việc áp dụng nguyên tắc chồng chập lượng tử cho vật thể lớn như con mèo dẫn tới kết luận phi lý với trực giác. Cách giải phổ biến là: khi mở hộp và quan sát, hàm sóng sụp đổ và mèo chỉ còn một trạng thái duy nhất là sống hoặc chết. Nhưng vì sao và khi nào sự sụp đổ xảy ra vẫn là đề tài tranh luận giữa các cách hiểu khác nhau về cơ học lượng tử.
- Quiz: Trước khi mở hộp, theo cách hiểu Copenhagen, con mèo được mô tả ra sao? — A. Chắc chắn còn sống; B. Chắc chắn đã chết; C. Ở trạng thái chồng chập vừa sống vừa chết (Đáp án: C)
- Nguồn: https://en.wikipedia.org/wiki/Schr%C3%B6dinger%27s_cat

### NL-078 — Nghịch lý Olbers (Olbers' paradox) [Vật lý]
- Câu đố: Nếu vũ trụ vô hạn, tồn tại vĩnh viễn và chứa sao ở khắp mọi nơi một cách đồng đều, thì nhìn về bất kỳ hướng nào trên bầu trời, tầm mắt ta cuối cùng cũng sẽ chạm tới bề mặt một ngôi sao. Vậy bầu trời đêm phải sáng rực như bề mặt sao ở mọi điểm. Vì sao bầu trời đêm lại tối?
- Lời giải: Nghịch lý chỉ ra rằng ít nhất một trong các giả định ban đầu phải sai: vũ trụ không vô hạn, không vĩnh viễn, hoặc sao không phân bố đồng đều mãi mãi. Lời giải được chấp nhận ngày nay là vũ trụ có tuổi hữu hạn và đang giãn nở, nên ánh sáng từ nhiều ngôi sao xa chưa kịp tới mắt ta. Nhờ đó, một câu hỏi tưởng như ngây thơ đã góp phần hé lộ tuổi hữu hạn của vũ trụ.
- Nguồn: https://en.wikipedia.org/wiki/Olbers%27_paradox

### NL-079 — Nghịch lý EPR (EPR paradox) [Vật lý]
- Câu đố: Einstein, Podolsky và Rosen tưởng tượng hai hạt vướng víu lượng tử rồi bay ra xa nhau. Đo hạt này dường như lập tức quyết định trạng thái của hạt kia, dù hai hạt cách nhau rất xa. Nếu đúng vậy, chẳng phải thông tin đã truyền đi nhanh hơn ánh sáng, vi phạm thuyết tương đối hay sao?
- Lời giải: Nghịch lý EPR được nêu ra để cho rằng cơ học lượng tử còn thiếu sót, vì nó dường như cho phép ảnh hưởng tức thời ở khoảng cách xa. Các thí nghiệm sau này xác nhận hiện tượng vướng víu là có thật, nhưng cũng cho thấy không thể dùng nó để gửi thông tin nhanh hơn ánh sáng. Vì vậy vướng víu không vi phạm thuyết tương đối, dù bản chất của nó vẫn khiến nhiều người băn khoăn.
- Quiz: Vướng víu lượng tử có cho phép gửi tin nhắn nhanh hơn ánh sáng không? — A. Có, đó chính là điểm mâu thuẫn của nghịch lý EPR; B. Không, vì không thể dùng vướng víu để truyền thông tin theo ý muốn; C. Có, nhưng chỉ với hai hạt ở rất gần nhau (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Einstein%E2%80%93Podolsky%E2%80%93Rosen_paradox

### NL-080 — Nghịch lý thông tin hố đen (Black hole information paradox) [Vật lý]
- Câu đố: Một vật rơi vào hố đen mang theo thông tin về chính nó, chẳng hạn cấu tạo của nó ra sao. Theo lý thuyết, hố đen sẽ dần bốc hơi qua bức xạ Hawking rồi biến mất hoàn toàn. Nếu hố đen biến mất mà bức xạ thoát ra không mang theo thông tin đó, thì thông tin đã đi đâu — phải chăng nó bị hủy diệt vĩnh viễn?
- Lời giải: Vấn đề là cơ học lượng tử khẳng định thông tin không bao giờ bị hủy diệt, trong khi bức tranh hố đen bốc hơi dường như cho thấy thông tin biến mất cùng hố đen. Nhiều nhà vật lý cho rằng thông tin thực ra được mã hóa trong bức xạ Hawking theo cách rất tinh vi, hoặc lưu lại ở chân trời sự kiện. Đây vẫn là một trong những câu hỏi mở lớn nhất nối liền cơ học lượng tử với thuyết tương đối rộng.
- Nguồn: https://en.wikipedia.org/wiki/Black_hole_information_paradox

### NL-081 — Nghịch lý Gibbs (Gibbs paradox) [Vật lý]
- Câu đố: Lấy hai bình chứa cùng một loại khí lý tưởng, cùng nhiệt độ và áp suất, rồi mở vách ngăn cho chúng trộn vào nhau. Vì hai khí giống hệt nhau nên chẳng có gì thật sự thay đổi, vậy entropy của hệ không nên tăng. Nhưng nếu tính theo công thức trộn khí thông thường, entropy lại tăng lên — phép tính sai ở đâu?
- Lời giải: Nghịch lý xuất phát từ việc coi các hạt khí giống hệt nhau như thể chúng có thể phân biệt được với nhau, khiến phép đếm trạng thái bị nhân lên thừa. Khi tính đúng rằng hoán đổi hai hạt giống hệt nhau không tạo ra trạng thái mới, entropy trộn của hai khí giống nhau trở về bằng không. Lời giải này cũng là một gợi ý sớm rằng các hạt trong tự nhiên là không thể phân biệt được.
- Nguồn: https://en.wikipedia.org/wiki/Gibbs_paradox

### NL-082 — Con quỷ của Maxwell (Maxwell's demon) [Vật lý]
- Câu đố: James Clerk Maxwell tưởng tượng một con quỷ tí hon canh một cánh cửa nhỏ giữa hai ngăn khí, nó chỉ mở cửa cho phân tử nhanh sang một bên và phân tử chậm sang bên kia. Dần dần một bên nóng lên và một bên lạnh đi mà không tốn năng lượng nào, như thể ta có được chênh lệch nhiệt độ miễn phí. Chẳng phải con quỷ đã phá vỡ định luật hai nhiệt động lực học hay sao?
- Lời giải: Con quỷ dường như làm giảm entropy của hệ mà không tốn công, mâu thuẫn với định luật cho rằng entropy chỉ có thể tăng. Lời giải hiện đại chỉ ra rằng con quỷ phải thu thập và xử lý thông tin về từng phân tử, và chính việc đo đạc, ghi nhớ rồi xóa thông tin đó cũng tốn năng lượng. Khi tính đủ chi phí của thông tin, định luật hai vẫn đứng vững.
- Quiz: Con quỷ của Maxwell cuối cùng bị hóa giải nhờ yếu tố nào? — A. Con quỷ không đủ nhanh để đóng mở cửa; B. Chi phí năng lượng của việc đo đạc và xóa thông tin; C. Khí trong hộp không đủ nóng (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Maxwell%27s_demon

### NL-083 — Hiệu ứng Mpemba (Mpemba effect) [Vật lý]
- Câu đố: Hai cốc nước giống hệt nhau đặt vào cùng một tủ đông, một cốc nước nóng và một cốc nước lạnh. Theo trực giác, cốc nước lạnh phải đóng băng trước vì nó đã gần điểm đóng băng hơn. Nhưng trong một số điều kiện, cốc nước nóng lại đóng băng nhanh hơn — làm sao nước nóng có thể vượt qua nước lạnh khi nó buộc phải đi qua đúng nhiệt độ của nước lạnh?
- Lời giải: Đây là hiệu ứng quan sát chứ không phải nghịch lý logic thuần túy, và nó không xảy ra trong mọi điều kiện mà chỉ trong một số cách bố trí thí nghiệm nhất định. Các lời giải nhắc tới nhiều yếu tố cùng lúc như đối lưu, bay hơi, khí hòa tan và hiện tượng quá lạnh của nước. Vì kết quả phụ thuộc mạnh vào điều kiện thí nghiệm nên hiệu ứng này vẫn gây tranh luận mỗi khi có nghiên cứu mới.
- Nguồn: https://en.wikipedia.org/wiki/Mpemba_effect

### NL-084 — Nghịch lý D'Alembert (D'Alembert's paradox) [Vật lý]
- Câu đố: Năm 1752, nhà toán học D'Alembert chứng minh rằng một vật chuyển động đều trong dòng chất lỏng lý tưởng không nhớt sẽ không chịu lực cản nào. Nhưng thực tế ai cũng biết một quả bóng lăn trong nước hay một chiếc xe chạy trong không khí đều bị cản lại rõ rệt. Lý thuyết tính ra lực cản bằng không, còn thực tế thì lực cản hiển nhiên có — bên nào sai?
- Lời giải: Nghịch lý nằm ở giả định lý tưởng hóa: chất lỏng trong phép tính của D'Alembert hoàn toàn không có độ nhớt. Trong chất lỏng thật, độ nhớt dù nhỏ vẫn tạo ra lớp biên mỏng sát bề mặt vật, và chính lớp này sinh ra lực cản. Khi tính thêm độ nhớt, lý thuyết và thực nghiệm gặp nhau, và nghịch lý được coi là đã giải quyết.
- Nguồn: https://en.wikipedia.org/wiki/D%27Alembert%27s_paradox

### NL-085 — Nghịch lý thủy tĩnh (Hydrostatic paradox) [Vật lý]
- Câu đố: Ba bình có cùng diện tích đáy và cùng chiều cao mực nước, nhưng hình dáng khác nhau: một bình loe ra, một bình thắt lại, một bình thẳng đứng. Lượng nước trong ba bình rất khác nhau, nên trọng lượng nước cũng khác nhau. Thế mà áp lực nước tác dụng lên đáy ba bình lại bằng nhau — làm sao đáy bình chứa ít nước lại chịu lực lớn bằng đáy bình chứa nhiều nước?
- Lời giải: Áp suất ở đáy chỉ phụ thuộc vào chiều cao cột nước chứ không phụ thuộc vào tổng lượng nước trong bình. Phần lực còn thiếu hoặc thừa được bù bởi thành bình: thành nghiêng sẽ chịu một phần trọng lượng nước hoặc đẩy thêm xuống đáy. Khi tính cả lực tác dụng lên thành bình, mọi con số đều khớp và nghịch lý biến mất.
- Quiz: Áp lực nước lên đáy bình phụ thuộc vào yếu tố nào? — A. Tổng lượng nước trong bình; B. Chiều cao cột nước phía trên đáy; C. Hình dáng của miệng bình (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Hydrostatic_paradox

### NL-086 — Nghịch lý Levinthal (Levinthal's paradox) [Vật lý]
- Câu đố: Một chuỗi protein có thể gấp theo số cách khổng lồ, ước tính tới 10^300 cấu hình khác nhau. Nếu protein thử từng cấu hình một cách ngẫu nhiên, nó sẽ cần thời gian lâu hơn cả tuổi của vũ trụ mới tìm ra hình dạng đúng. Thế mà trong thực tế protein gấp xong chỉ trong tích tắc — nó tìm đường nhanh như vậy bằng cách nào?
- Lời giải: Nghịch lý cho thấy protein không thể gấp bằng cách thử mò từng cấu hình một cách ngẫu nhiên. Lời giải là quá trình gấp đi theo một cảnh quan năng lượng có hình phễu, dẫn dắt chuỗi protein từng bước về trạng thái ổn định thay vì lang thang khắp mọi khả năng. Nhờ đó, một bài toán tìm kiếm tưởng như không thể lại được giải trong thời gian rất ngắn.
- Nguồn: https://en.wikipedia.org/wiki/Levinthal%27s_paradox

### NL-087 — Nghịch lý Peto (Peto's paradox) [Vật lý]
- Câu đố: Ung thư về cơ bản bắt đầu từ những lỗi xảy ra khi tế bào phân chia, vậy sinh vật càng nhiều tế bào và càng sống lâu thì càng có nhiều cơ hội mắc ung thư. Cá voi có số tế bào gấp hàng nghìn lần con người và sống hàng chục năm, lẽ ra phải mắc ung thư thường xuyên hơn hẳn. Nhưng thực tế cá voi lại rất hiếm khi mắc ung thư — vì sao kẻ có nhiều tế bào nhất lại ít ung thư nhất?
- Lời giải: Nghịch lý cho thấy số tế bào không phải là yếu tố duy nhất quyết định nguy cơ ung thư, vì tiến hóa đã trang bị thêm các cơ chế bảo vệ cho loài lớn. Cá voi và voi được cho là có nhiều bản sao của các gen ức chế khối u và cơ chế sửa chữa ADN hiệu quả hơn. Nghiên cứu các cơ chế này đang gợi ý những hướng mới cho việc phòng chống ung thư ở người.
- Nguồn: https://en.wikipedia.org/wiki/Peto%27s_paradox

### NL-088 — Nghịch lý sinh vật phù du (Paradox of the plankton) [Vật lý]
- Câu đố: Trong mặt nước biển, hàng trăm loài thực vật phù du cùng tranh nhau chỉ vài nguồn tài nguyên giống nhau: ánh sáng, nitơ, phốt pho và vài chất khác. Theo nguyên tắc loại trừ cạnh tranh, loài giỏi nhất với mỗi nguồn tài nguyên sẽ dần đánh bật các loài khác, chỉ còn vài loài sống sót. Vì sao thực tế lại có rất nhiều loài phù du cùng tồn tại trong cùng một vùng nước?
- Lời giải: Nghịch lý thách thức nguyên tắc loại trừ cạnh tranh vốn dự đoán rằng số loài cùng tồn tại không thể vượt quá số nguồn tài nguyên. Các lời giải nhấn mạnh rằng môi trường biển không bao giờ đứng yên: dòng chảy, mùa vụ và sự xáo trộn liên tục mở ra những cơ hội mới cho các loài khác nhau. Nhờ đó, sự đa dạng được duy trì ngay cả khi các loài tưởng như đang tranh nhau cùng một thứ.
- Nguồn: https://en.wikipedia.org/wiki/Paradox_of_the_plankton

### NL-089 — Nghịch lý Moravec (Moravec's paradox) [Logic]
- Câu đố: Máy tính đánh bại kiện tướng cờ vua và giải toán cao cấp, những việc con người phải học nhiều năm mới làm được. Nhưng cùng một cỗ máy đó lại chật vật với việc nhặt một con ốc ra khỏi hộp ốc, hay bước đi vững vàng trên mặt đất gồ ghề — những việc trẻ con làm một cách tự nhiên. Vì sao việc khó với người lại dễ với máy, còn việc dễ với người lại khó với máy?
- Lời giải: Nghịch lý chỉ ra rằng trí tuệ con người không xếp theo độ khó mà ta cảm nhận: tư duy trừu tượng là kỹ năng mới nên ta thấy nó khó, còn cảm nhận và vận động là kỹ năng cổ xưa đã được tiến hóa mài giũa hàng triệu năm. Máy tính giỏi ở những gì có quy tắc rõ ràng, nhưng kém ở những gì đòi hỏi cảm nhận cơ thể và tương tác với thế giới thật. Vì vậy, tự động hóa việc chân tay khó hơn nhiều so với dự đoán ban đầu của ngành trí tuệ nhân tạo.
- Quiz: Theo nghịch lý Moravec, việc nào khó hơn với robot? — A. Chơi cờ vua ở trình độ kiện tướng; B. Nhặt một con ốc ra khỏi hộp đầy ốc; C. Tính nhẩm phép nhân nhiều chữ số (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Moravec%27s_paradox

### NL-090 — Nghịch lý của sự lựa chọn (Paradox of choice) [Logic]
- Câu đố: Một cửa hàng bán 3 loại mứt thì khách mua vui vẻ, nhưng khi bày ra 30 loại mứt thì khách lại mua ít hơn và kém hài lòng hơn. Thêm lựa chọn lẽ ra phải giúp ta tìm được thứ hợp ý hơn, vậy mà càng nhiều lựa chọn, ta càng khó quyết định và càng dễ tiếc nuối. Vì sao tự do lựa chọn nhiều hơn lại khiến ta khổ sở hơn?
- Lời giải: Nghịch lý này cho thấy lựa chọn chỉ có ích tới một mức nào đó, vượt quá mức đó thì chi phí suy nghĩ và nỗi sợ chọn sai sẽ lấn át lợi ích. Người ta bắt đầu so sánh không ngừng, lo rằng lựa chọn khác tốt hơn, và đổ lỗi cho bản thân nếu kết quả chưa vừa ý. Vì vậy, giới hạn số lựa chọn hoặc đặt ra tiêu chuẩn đủ tốt đôi khi lại mang tới sự hài lòng cao hơn.
- Quiz: Khi có quá nhiều lựa chọn, người ta thường ra sao? — A. Quyết định nhanh hơn và hài lòng hơn; B. Khó quyết định hơn và dễ tiếc nuối hơn; C. Luôn chọn được phương án tốt nhất (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/The_Paradox_of_Choice

### NL-091 — Nghịch lý của sự khoan dung (Paradox of tolerance) [Logic]
- Câu đố: Một xã hội khoan dung cam kết chấp nhận mọi quan điểm, kể cả quan điểm không khoan dung. Nhưng nếu xã hội dung túng cho những nhóm muốn xóa bỏ sự khoan dung, thì chính sự khoan dung sẽ bị tiêu diệt. Vậy một xã hội khoan dung có nên khoan dung với sự không khoan dung hay không?
- Lời giải: Nghịch lý chỉ ra rằng khoan dung tuyệt đối sẽ tự hủy diệt, vì nó trao quyền cho kẻ muốn chấm dứt khoan dung. Triết gia Karl Popper kết luận rằng xã hội khoan dung có quyền không khoan dung với sự không khoan dung, đặc biệt khi nó dùng bạo lực hoặc đe dọa tự do thảo luận. Nhờ giới hạn này, khoan dung mới có thể tồn tại lâu dài thay vì tự tay đào hố chôn mình.
- Nguồn: https://en.wikipedia.org/wiki/Paradox_of_tolerance

### NL-092 — Nghịch lý của chủ nghĩa khoái lạc (Paradox of hedonism) [Logic]
- Câu đố: Một người quyết tâm chỉ theo đuổi hạnh phúc: ngày nào cũng tự hỏi mình có đang vui không, có đang hạnh phúc không. Càng chăm chăm đo đếm hạnh phúc, người đó càng thấy mình chưa đủ vui và càng khổ sở. Nhưng một người khác mải mê với công việc hay giúp đỡ người khác, chẳng nghĩ gì tới hạnh phúc, lại thấy mình hạnh phúc — vì sao càng đuổi theo hạnh phúc thì càng không bắt được nó?
- Lời giải: Nghịch lý cho thấy hạnh phúc thường là sản phẩm phụ của việc theo đuổi những điều có ý nghĩa, chứ không phải mục tiêu có thể nhắm thẳng mà đạt được. Khi hạnh phúc trở thành mục tiêu duy nhất, ta liên tục soi xét cảm xúc của mình và biến mọi trải nghiệm thành bài kiểm tra. Vì vậy, các triết gia khuyên nên tập trung vào hoạt động và giá trị, để hạnh phúc tự đến như một hệ quả.
- Nguồn: https://en.wikipedia.org/wiki/Paradox_of_hedonism

### NL-093 — Nghịch lý toàn năng (Omnipotence paradox) [Logic]
- Câu đố: Nếu có một đấng toàn năng, đấng ấy có thể tạo ra một tảng đá nặng tới mức chính mình cũng không nhấc nổi hay không? Nếu tạo được, thì có một việc đấng ấy không làm được là nhấc tảng đá đó, nên không còn toàn năng. Nếu không tạo được, thì cũng có một việc đấng ấy không làm được, nên cũng không toàn năng — vậy toàn năng có thể tồn tại không?
- Lời giải: Nghịch lý dùng chính định nghĩa toàn năng để chống lại nó: dù trả lời có hay không, ta cũng suy ra đấng toàn năng bị giới hạn. Một lời giải phổ biến là toàn năng chỉ bao gồm những việc có thể xảy ra một cách logic, còn tảng đá như trên là một khái niệm tự mâu thuẫn nên không tính. Lời giải khác cho rằng khái niệm toàn năng tuyệt đối vốn đã mơ hồ và cần được định nghĩa lại chặt chẽ hơn.
- Quiz: Câu hỏi về tảng đá quá nặng chủ yếu cho thấy điều gì? — A. Đấng toàn năng chắc chắn không tồn tại; B. Khái niệm toàn năng tuyệt đối có thể tự mâu thuẫn nếu hiểu theo nghĩa đen; C. Tảng đá quá nặng là không thể tạo ra về mặt vật lý (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Omnipotence_paradox

### NL-094 — Nghịch lý của cái ác (Problem of evil) [Logic]
- Câu đố: Giả sử có một đấng toàn năng, toàn tri và toàn thiện, thì vì sao trên đời vẫn có đau khổ và cái ác, kể cả nỗi đau của những người vô tội? Nếu đấng ấy muốn ngăn cái ác mà không ngăn được, thì không toàn năng. Nếu ngăn được mà không muốn ngăn, thì không toàn thiện — vậy làm sao ba thuộc tính ấy cùng tồn tại với cái ác?
- Lời giải: Đây là một trong những thách thức lâu đời nhất đối với thần học, vì nó đặt ba thuộc tính của đấng tối cao vào thế mâu thuẫn với thực tế đau khổ. Các lời giải thường viện tới ý chí tự do của con người, cho rằng một thế giới có tự do tất yếu cho phép con người chọn sai, hoặc cho rằng đau khổ phục vụ mục đích lớn hơn mà ta chưa thấy hết. Đến nay, chưa có lời giải nào khiến cả hai phía đều hài lòng.
- Nguồn: https://en.wikipedia.org/wiki/Problem_of_evil

### NL-095 — Nghịch lý dịch chuyển tức thời (Teletransportation paradox) [Logic]
- Câu đố: Một cỗ máy quét toàn bộ cơ thể bạn, phá hủy bản gốc trên Trái Đất rồi tái tạo một bản sao giống hệt từng nguyên tử trên Sao Hỏa, với đầy đủ ký ức và tính cách của bạn. Người bước ra trên Sao Hỏa có phải là bạn không, hay bạn đã chết và đó chỉ là một bản sao? Nếu cỗ máy trục trặc và không phá hủy bản gốc, thì trên đời có hai bạn — ai mới là bạn thật?
- Lời giải: Nghịch lý của Parfit cho thấy trực giác của ta về bản sắc cá nhân không đủ rõ ràng để trả lời dứt khoát. Khi có hai bản sao giống hệt nhau cùng tuyên bố là bạn, không có tiêu chí nào phân biệt được ai mới là bạn thật. Parfit kết luận rằng câu hỏi ai là ai có thể là câu hỏi sai, điều quan trọng là sự tiếp nối tâm lý chứ không phải một bản sắc bí ẩn nào đó.
- Quiz: Nếu máy dịch chuyển tạo ra bản sao trên Sao Hỏa mà không phá hủy bản gốc, điều gì xảy ra? — A. Chỉ có một người là bạn thật, người kia là giả; B. Có hai người cùng có ký ức và tính cách của bạn, và không có tiêu chí rõ ràng để chọn ai là bạn; C. Cả hai đều biến mất (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Teletransportation_paradox

### NL-096 — Cỗ máy trải nghiệm (Experience machine) [Logic]
- Câu đố: Robert Nozick tưởng tượng một cỗ máy có thể cho bạn mọi trải nghiệm mình muốn suốt đời: tình yêu hoàn hảo, danh vọng, thành công, mà bạn không hề biết đó chỉ là mô phỏng. Nếu hạnh phúc và trải nghiệm dễ chịu là tất cả những gì quan trọng, bạn nên cắm vào cỗ máy mãi mãi. Nhưng hầu hết mọi người đều từ chối — vì sao ta lại từ chối một cuộc đời toàn niềm vui?
- Lời giải: Thí nghiệm cho thấy con người coi trọng nhiều thứ ngoài cảm giác dễ chịu, chẳng hạn được thật sự làm việc, thật sự yêu thương và sống trong thực tế. Nếu chỉ trải nghiệm mới quan trọng, việc từ chối cỗ máy sẽ là phi lý, vậy mà đa số đều từ chối. Nozick kết luận rằng chủ nghĩa khoái lạc đã bỏ sót điều quan trọng: ta muốn sống một cuộc đời thật, chứ không chỉ mơ một giấc mơ đẹp.
- Quiz: Đa số mọi người từ chối cỗ máy trải nghiệm vì lý do nào? — A. Vì cỗ máy quá đắt; B. Vì họ coi trọng việc thật sự sống và làm điều thật, không chỉ cảm thấy như thật; C. Vì họ sợ máy bị hỏng giữa chừng (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Experience_machine

### NL-097 — Căn phòng tiếng Trung (Chinese room) [Logic]
- Câu đố: Một người không biết tiếng Trung bị nhốt trong phòng, chỉ có một cuốn sổ quy tắc bằng tiếng Anh hướng dẫn cách biến các ký tự Trung nhận được thành các ký tự Trung trả lời. Người ngoài đưa câu hỏi tiếng Trung vào, nhận lại câu trả lời trôi chảy và tưởng rằng trong phòng có người hiểu tiếng Trung. Nhưng người trong phòng thật sự có hiểu tiếng Trung không — và một cỗ máy làm đúng như vậy thì có hiểu không?
- Lời giải: John Searle lập luận rằng làm theo quy tắc biến đổi ký hiệu không đồng nghĩa với hiểu nghĩa, dù kết quả bên ngoài trông giống hệt người hiểu thật. Từ đó ông cho rằng máy tính chỉ thao tác cú pháp thì không thể có ngữ nghĩa hay sự hiểu biết đích thực. Phản biện nổi tiếng nhất là cả hệ thống gồm người, sổ quy tắc và căn phòng mới là thứ hiểu, chứ không phải riêng người trong phòng.
- Nguồn: https://en.wikipedia.org/wiki/Chinese_room

### NL-098 — Căn phòng của Mary (Lập luận tri thức) (Mary's room) [Logic]
- Câu đố: Mary là nhà khoa học biết mọi sự thật vật lý về màu sắc và thị giác, nhưng cả đời chỉ sống trong căn phòng đen trắng và chưa từng thấy màu sắc. Một ngày cô bước ra ngoài và lần đầu nhìn thấy một bông hồng đỏ. Liệu cô có học được điều gì mới không — và nếu có, thì tri thức vật lý đầy đủ kia hóa ra vẫn chưa đầy đủ hay sao?
- Lời giải: Lập luận của Frank Jackson cho rằng Mary học được điều mới là cảm giác thấy màu đỏ trông như thế nào, một điều mà mọi sự thật vật lý cũng không truyền đạt được. Nếu đúng vậy, sẽ tồn tại những sự thật phi vật lý mà chủ nghĩa duy vật không bao quát hết. Phản biện phổ biến là Mary không học thêm sự thật mới mà chỉ có thêm khả năng nhận biết và tưởng tượng màu đỏ.
- Quiz: Lập luận căn phòng của Mary chủ yếu thách thức quan điểm nào? — A. Chủ nghĩa duy vật cho rằng mọi sự thật đều là sự thật vật lý; B. Thuyết tiến hóa; C. Thuyết tương đối (Đáp án: A)
- Nguồn: https://en.wikipedia.org/wiki/Knowledge_argument

### NL-099 — Zombie triết học (Philosophical zombie) [Logic]
- Câu đố: Hãy tưởng tượng một sinh vật giống hệt bạn về mọi mặt vật lý: cùng bộ não, cùng hành vi, cùng cách nói cười và phản ứng với thế giới. Điểm khác duy nhất là bên trong nó hoàn toàn tối đen, không có bất kỳ trải nghiệm chủ quan nào, không cảm thấy đau, vui hay thấy màu đỏ. Nếu một sinh vật như vậy có thể tưởng tượng được một cách nhất quán, thì ý thức có thật sự chỉ là vật chất hay không?
- Lời giải: Lập luận zombie cho rằng nếu ta có thể hình dung một bản sao vật lý hoàn hảo mà không có ý thức, thì ý thức không thể suy ra một cách logic từ các sự thật vật lý. Từ đó, một số triết gia kết luận rằng ý thức là một khía cạnh riêng của thực tại, không rút gọn được về vật chất. Phe phản biện đáp rằng tưởng tượng được không có nghĩa là có thể thật, giống như ta có thể tưởng tượng nước không phải là H2O.
- Nguồn: https://en.wikipedia.org/wiki/Philosophical_zombie

### NL-100 — Nghịch lý Loschmidt (Loschmidt's paradox) [Vật lý]
- Câu đố: Các định luật vật lý ở cấp độ vi mô đều đối xứng theo thời gian: một đoạn phim về các phân tử va chạm nhau khi chạy ngược vẫn tuân thủ đúng định luật. Thế nhưng ở cấp độ vĩ mô, entropy chỉ tăng theo một chiều, tách trà nóng chỉ nguội đi chứ không bao giờ tự nóng lên. Vì sao một thế giới vi mô không phân biệt quá khứ và tương lai lại sinh ra một thế giới vĩ mô có mũi tên thời gian rõ rệt?
- Lời giải: Nghịch lý chỉ ra mâu thuẫn giữa tính đảo ngược của cơ học vi mô và tính không đảo ngược của nhiệt động lực học. Lời giải của Boltzmann cho rằng entropy tăng là chuyện thống kê: có nhiều cách để hệ trở nên lộn xộn hơn là ngăn nắp, nên chiều tăng entropy là chiều có xác suất áp đảo. Nhờ đó, mũi tên thời gian không nằm trong từng định luật mà nảy sinh từ điều kiện ban đầu ít entropy của vũ trụ.
- Nguồn: https://en.wikipedia.org/wiki/Loschmidt%27s_paradox

### NL-101 — Nghịch lý phiên tòa (Paradox of the Court) [Logic]
- Câu đố: Nhà hùng biện Protagoras dạy luật cho học trò Euathlus với thỏa thuận: chỉ trả học phí sau khi Euathlus thắng vụ kiện đầu tiên. Euathlus học xong thì không nhận vụ nào, nên Protagoras kiện đòi tiền. Protagoras nói: nếu ta thắng, tòa buộc trò trả; nếu ta thua, trò đã thắng vụ đầu tiên nên theo thỏa thuận vẫn phải trả. Euathlus đáp: nếu ta thắng, tòa phán ta không phải trả; nếu ta thua, ta vẫn chưa thắng vụ nào nên theo thỏa thuận cũng không phải trả. Ai đúng?
- Lời giải: Cả hai đều tráo đổi hai luật chơi: phán quyết của tòa và điều khoản trong thỏa thuận, trong khi vụ kiện này lại tự làm thay đổi sự thật mà thỏa thuận nói tới. Cách gỡ được nhiều luật gia chấp nhận là tách vụ kiện thành hai thời điểm: vụ đầu Euathlus thắng vì lúc đó cậu chưa thắng vụ nào, rồi chính chiến thắng ấy khiến học phí đến hạn và Protagoras thắng vụ kiện thứ hai. Nghịch lý tan khi ta thấy thời gian làm thay đổi điều kiện, thay vì coi mọi lập luận đều đúng cùng một lúc.
- Quiz: Theo cách gỡ được nhiều luật gia hiện đại chấp nhận, kết quả cuối cùng ra sao? — A. Euathlus thắng vụ kiện đầu, rồi thua vụ kiện thứ hai và phải trả học phí; B. Protagoras thắng ngay vụ kiện đầu tiên; C. Tòa tuyên cả hai cùng thua và hợp đồng bị hủy (Đáp án: A)
- Nguồn: https://en.wikipedia.org/wiki/Paradox_of_the_Court

### NL-102 — Nghịch lý tình bạn (Friendship paradox) [Xác suất]
- Câu đố: Hãy đếm số bạn thân của bạn, rồi đếm số bạn thân trung bình của từng người bạn ấy. Nhà xã hội học Scott Feld phát hiện năm 1991 rằng hầu hết mọi người đều có ít bạn hơn bạn bè của mình. Nghe thật oan ức: chẳng lẽ bạn bè ai cũng nổi tiếng hơn mình? Hiện tượng này đúng với hầu hết mọi người trong mọi mạng xã hội, từ lớp học tới mạng xã hội trực tuyến.
- Lời giải: Người càng nhiều bạn thì càng có mặt trong vòng bạn bè của nhiều người, nên khi bạn nhìn vào bạn bè của mình, bạn đã vô tình lấy mẫu thiên về những người nổi tiếng. Đây là một dạng thiên lệch lấy mẫu, không phải vì bạn kém hấp dẫn hay bạn bè bạn đặc biệt gì. Toán học đằng sau nó liên quan tới bất đẳng thức trung bình cộng và trung bình nhân, và hiệu ứng biến mất nếu ta đếm toàn bộ mạng lưới thay vì chỉ nhìn từ góc của một người.
- Quiz: Vì sao bạn bè của bạn thường có nhiều bạn hơn bạn? — A. Vì bạn ít hấp dẫn hơn bạn bè của mình; B. Vì người nhiều bạn xuất hiện trong vòng bạn của nhiều người hơn, nên mẫu bạn nhìn thấy đã bị lệch; C. Vì mọi người đều nói dối về số bạn của mình (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Friendship_paradox

### NL-103 — Nghịch lý chờ xe buýt (Inspection paradox) [Xác suất]
- Câu đố: Xe buýt trung bình cứ 20 phút lại có một chuyến, nhưng bạn ra bến vào một lúc ngẫu nhiên và thường phải chờ lâu hơn 10 phút. Sao lại thế? Giả sử một nửa các khoảng cách giữa hai chuyến là 10 phút, một nửa là 30 phút. Bạn có khả năng gấp ba lần rơi vào khoảng 30 phút so với khoảng 10 phút, vì khoảng dài chiếm nhiều thời gian hơn trong ngày. Thời gian chờ trung bình của bạn vì thế là 12,5 phút chứ không phải 10 phút.
- Lời giải: Khi bạn đến bến vào lúc ngẫu nhiên, bạn không lấy mẫu các khoảng chờ một cách đều nhau mà lấy mẫu theo độ dài của chúng, nên khoảng dài bị đại diện quá mức. Đây gọi là lấy mẫu thiên về kích thước, và nó giải thích cả chuyện vì sao lớp học bạn ngồi thường đông hơn lớp trung bình của trường. Nghịch lý biến mất khi mọi khoảng đều bằng nhau, vì lúc đó không còn gì để lệch nữa.
- Nguồn: https://en.wikipedia.org/wiki/Renewal_theory

### NL-104 — Nghịch lý làm giàu hệ sinh thái (Paradox of enrichment) [Vật lý]
- Câu đố: Trong một hồ nước, bạn bón thêm phân để tảo (thức ăn của loài giáp xác) phát triển, mong cả tảo lẫn loài ăn tảo đều sống khỏe hơn. Nhà sinh thái Michael Rosenzweig chỉ ra năm 1971 rằng làm vậy có thể khiến hệ sinh thái mất ổn định và loài săn mồi tuyệt chủng. Thêm thức ăn cho con mồi lại giết chết kẻ săn mồi, nghe thật ngược đời. Vậy cho ăn nhiều hơn sao lại nguy hiểm?
- Lời giải: Khi con mồi dồi dào, quần thể săn mồi bùng nổ rồi ăn sạch con mồi, sau đó chính nó cũng sụp đổ vì đói, tạo thành dao động ngày càng lớn. Toán học gọi đây là phân nhánh Hopf: vượt một ngưỡng giàu có nhất định, điểm cân bằng ổn định biến thành vòng lặp dao động mà đáy của nó chạm gần bằng không. Trong thực tế, nơi trú ẩn của con mồi và môi trường không đồng đều có thể cứu hệ sinh thái khỏi vòng xoáy này.
- Nguồn: https://en.wikipedia.org/wiki/Paradox_of_enrichment

### NL-105 — Nghịch lý giá trị: nước rẻ hơn kim cương (Paradox of value) [Quyết định]
- Câu đố: Nước là thứ không thể thiếu để sống, kim cương chỉ để trang trí, vậy mà một viên kim cương nhỏ có giá bằng cả một xe bồn nước. Adam Smith nêu nghịch lý này trong cuốn Của cải của các dân tộc, và nó từng làm đau đầu các nhà kinh tế suốt hàng thế kỷ. Nếu giá phản ánh mức độ hữu ích, vì sao thứ vô dụng hơn lại đắt hơn nhiều? Người sắp chết khát giữa sa mạc sẽ trả bao nhiêu cho một ly nước?
- Lời giải: Giá không do tổng ích lợi của cả loại hàng quyết định mà do ích lợi biên của từng đơn vị thêm vào: ly nước thứ trăm gần như vô giá trị khi nước đã dồi dào, còn viên kim cương hiếm hoi vẫn rất đáng thèm muốn. Người sắp chết khát sẽ trả mọi thứ cho ly nước đầu tiên, vì với anh ta ích lợi biên của nước lúc đó cao hơn kim cương rất nhiều. Kinh tế học biên tế đã giải quyết nghịch lý này vào thế kỷ 19 bằng cách phân biệt giá trị sử dụng tổng thể và giá trị của đơn vị cuối cùng.
- Quiz: Vì sao kim cương đắt hơn nước dù nước hữu ích hơn nhiều? — A. Vì kim cương tốn nhiều công sức khai thác hơn nước; B. Vì giá do ích lợi biên của từng đơn vị quyết định, không phải tổng ích lợi của cả loại hàng; C. Vì con người luôn thích thứ lấp lánh hơn thứ cần thiết (Đáp án: B)
- Nguồn: https://en.wikipedia.org/wiki/Paradox_of_value

### NL-106 — Nghịch lý Meno: làm sao tìm thứ mình chưa biết? (Meno's paradox) [Logic]
- Câu đố: Trong đối thoại Meno của Plato (khoảng năm 385 trước Công nguyên), Meno hỏi Socrates: làm sao ta tìm kiếm thứ mà ta chưa biết? Nếu ta đã biết nó là gì thì chẳng cần tìm, còn nếu ta chưa biết thì tìm cái gì, và khi vô tình vấp phải nó thì làm sao nhận ra đó chính là thứ mình tìm? Nghịch lý này khiến mọi việc học hỏi dường như bất khả thi. Socrates đã trả lời ra sao?
- Lời giải: Socrates đáp bằng thuyết hồi tưởng: linh hồn vốn đã biết mọi thứ từ trước khi nhập vào thân xác, nên học hỏi thực chất là nhớ lại, và câu hỏi gợi mở đúng cách sẽ khơi dậy tri thức ấy. Ông minh họa bằng cách dẫn dắt một nô lệ chưa từng học toán, chỉ bằng câu hỏi, tự tìm ra cách nhân đôi diện tích hình vuông. Ngày nay triết học vẫn dùng nghịch lý Meno để bàn về việc học, và nhiều người cho rằng ta luôn bắt đầu với một ít tri thức nền để nhận ra đáp án khi gặp nó.
- Nguồn: https://en.wikipedia.org/wiki/Meno

### NL-107 — Câu đố thuốc độc của Kavka (Kavka's toxin puzzle) [Quyết định]
- Câu đố: Một tỷ phú lập dị đưa cho bạn một lọ thuốc độc: uống vào sẽ đau đớn một ngày nhưng không nguy hiểm tính mạng và không để lại di chứng. Ông ta sẽ trả cho bạn một triệu đô vào sáng mai, nếu vào nửa đêm nay bạn thật lòng có ý định uống thuốc vào chiều mai. Bạn không cần thật sự uống mới nhận tiền, và hoàn toàn được đổi ý sau khi đã nhận tiền. Bạn có thể thật lòng định uống thuốc, trong khi biết rõ rằng sáng mai mình sẽ không bao giờ uống nó không?
- Lời giải: Kavka lập luận rằng người lý trí không thể thật lòng định làm việc mà chính mình biết là vô lý, vì ý định là khuynh hướng hành động dựa trên lý do chứ không phải lời tự nhủ suông. Khi tiền đã vào tài khoản, uống thuốc chẳng còn lợi ích nào, nên bạn biết trước mình sẽ không uống, và vì thế cũng không thể thật sự có ý định uống. Câu đố này tách rời tính hợp lý của việc có một ý định khỏi tính hợp lý của việc thực hiện nó, và nó bắt nguồn từ bài toán răn đe hạt nhân của Kavka.
- Nguồn: https://en.wikipedia.org/wiki/Kavka%27s_toxin_puzzle

### NL-108 — Nghịch lý Bertrand: ba đáp án cho một bài toán (Bertrand paradox (probability)) [Xác suất]
- Câu đố: Vẽ một tam giác đều nội tiếp trong một đường tròn, rồi chọn ngẫu nhiên một dây cung của đường tròn. Xác suất để dây cung đó dài hơn cạnh của tam giác là bao nhiêu? Joseph Bertrand đưa ra năm 1889 ba cách lập luận đều có vẻ đúng, nhưng cho ba đáp án khác nhau: một phần ba, một nửa và một phần tư. Cùng một bài toán, cùng một cách hỏi, sao lại có ba đáp án đúng?
- Lời giải: Ba cách chọn ngẫu nhiên thực ra là ba thí nghiệm khác nhau: chọn ngẫu nhiên hai đầu mút, chọn ngẫu nhiên một điểm trên bán kính, hay chọn ngẫu nhiên trung điểm trong hình tròn. Mỗi cách định nghĩa cụm từ chọn ngẫu nhiên một kiểu, nên mỗi cách cho một phân phối khác nhau và một đáp án khác nhau. Bài học của Bertrand là xác suất chỉ có nghĩa khi ta nói rõ cơ chế ngẫu nhiên, chứ cụm từ ngẫu nhiên một mình thì chưa đủ.
- Nguồn: https://en.wikipedia.org/wiki/Bertrand_paradox_(probability)

### NL-109 — Hiện tượng Will Rogers: chuyển người, cả hai nhóm đều khá lên (Will Rogers phenomenon) [Xác suất]
- Câu đố: Có hai nhóm: nhóm A gồm các số 1, 2, 3, 4 (trung bình 2,5) và nhóm B gồm các số 5, 6, 7, 8, 9 (trung bình 7). Chuyển số 5 từ nhóm B sang nhóm A, trung bình nhóm A tăng lên 3 và trung bình nhóm B tăng lên 7,5. Cả hai nhóm đều khá lên mà không một con số nào thay đổi, và trung bình toàn bộ vẫn là 5. Hiện tượng này được đặt theo câu đùa gán cho danh hài Will Rogers: người Oklahoma di cư sang California đã nâng trí tuệ trung bình của cả hai bang. Chuyện gì đang xảy ra?
- Lời giải: Số 5 nhỏ hơn trung bình nhóm B nên rời đi làm trung bình nhóm B tăng, đồng thời lớn hơn trung bình nhóm A nên gia nhập làm trung bình nhóm A tăng. Điều kiện duy nhất là giá trị được chuyển phải nằm giữa hai trung bình của hai nhóm, chứ không cần là số nhỏ nhất hay lớn nhất. Trong y học, hiện tượng này xuất hiện khi xét nghiệm tốt hơn chuyển bệnh nhân sang giai đoạn bệnh nặng hơn, khiến tỷ lệ sống của cả hai giai đoạn đều trông khá lên dù không ai sống lâu hơn.
- Nguồn: https://en.wikipedia.org/wiki/Will_Rogers_phenomenon
