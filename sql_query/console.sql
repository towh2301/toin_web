------- Insert Labels
INSERT INTO pages_product (type_id, en_title, vi_title, jp_title, en_description, vi_description, jp_description)
VALUES
-- 1. Tack Labels
(1, 'Tack Labels', 'Nhãn dính', 'タックラベル',
 'High-adhesion tack labels designed for secure attachment on various surfaces. Ideal for packaging, logistics, and industrial use.',
 'Nhãn dính có độ bám dính cao, thích hợp cho nhiều bề mặt khác nhau. Phù hợp trong đóng gói, vận chuyển và công nghiệp.',
 '高い粘着力を持つタックラベルで、さまざまな表面にしっかりと貼り付けられます。包装、物流、工業用途に最適です。'),

-- 2. Single-sheet Labels
(1, 'Single-sheet Labels', 'Nhãn đơn tờ', '単票ラベル',
 'High-quality single-sheet labels that offer flexibility and easy customization for printing. Perfect for small-batch or specialty products.',
 'Nhãn đơn tờ chất lượng cao, dễ dàng in ấn và tùy chỉnh. Thích hợp cho các sản phẩm đặc biệt hoặc số lượng nhỏ.',
 '高品質の単票ラベルで、印刷やカスタマイズが簡単です。少量生産や特別な製品に最適です。'),

-- 3. Delayed Labels
(1, 'Delayed Labels', 'Nhãn dính trễ', 'ディレイラベル',
 'Special delayed-adhesion labels that allow repositioning or time-delayed sticking for process flexibility.',
 'Nhãn dính trễ đặc biệt cho phép dán lại hoặc dán sau thời gian nhất định, giúp linh hoạt trong quy trình sản xuất.',
 '貼り付けを遅らせたり、位置を調整できる特殊なディレイラベルで、作業工程に柔軟性を持たせます。'),

-- 4. Glue Labels
(1, 'Glue Labels', 'Nhãn keo dán', '糊付けラベル',
 'Traditional glue-applied labels with excellent durability and smooth finish, suitable for glass, plastic, and paper containers.',
 'Nhãn sử dụng keo dán truyền thống, độ bền cao và bề mặt mịn, phù hợp cho chai lọ thủy tinh, nhựa và giấy.',
 '伝統的な糊付けタイプのラベルで、高い耐久性と滑らかな仕上がりを持ち、ガラス・プラスチック・紙容器に適しています。'),

-- 5. POP Labels
(1, 'POP Labels', 'Nhãn POP', 'POPラベル',
 'Eye-catching POP labels designed for product promotion, shelf display, and retail marketing impact.',
 'Nhãn POP nổi bật, dùng để quảng bá sản phẩm, trưng bày trên kệ và tăng hiệu quả tiếp thị bán lẻ.',
 '店頭での販促や陳列に効果的な、視覚的に目を引くPOPラベルです。');

------ Insert intructions
INSERT INTO pages_product (type_id, en_title, vi_title, jp_title, en_description, vi_description, jp_description)
VALUES (2, 'Instructions', 'Tờ hướng dẫn', '説明書',
        'From pharmaceuticals (medical/OTC use) to cosmetics, we produce instructions (package inserts) based on stringent quality standards that provide consumers with accurate product information.',
        'Từ dược phẩm (dùng trong y tế/không kê đơn) đến mỹ phẩm, chúng tôi đều viết hướng dẫn (tờ hướng dẫn sử dụng) dựa trên các tiêu chuẩn chất lượng nghiêm ngặt, cung cấp cho người tiêu dùng thông tin chính xác về sản phẩm.',
        '医薬品（医療用・OTC用）から化粧品まで、消費者に正確な製品情報を提供するための厳しい品質基準に基づいた説明書（添付文書）を制作しています。');


INSERT INTO pages_product (type_id, en_title, vi_title, jp_title, en_description, vi_description, jp_description, image)
VALUES
-- 1️⃣ Crush luster
(4, 'Crush Luster', 'Hiệu ứng ánh sáng Crush', 'クラッシュラスター',
 'This printing technology applies three-dimensional textures that reflect light randomly.',
 'Công nghệ in này tạo ra bề mặt có hiệu ứng ba chiều, phản chiếu ánh sáng ngẫu nhiên.',
 '光をランダムに反射する立体的な質感を持つ印刷技術です。', 'product/crush_luster.jpg'),

-- 2️⃣ Hot stamping delayed labels
(4, 'Hot Stamping Delayed Labels', 'Nhãn dính trễ ép nhiệt', 'ホットスタンピングディレイラベル',
 'These high-quality delayed labels may be embossed using specialized equipment.',
 'Nhãn dính trễ chất lượng cao có thể được ép nổi bằng thiết bị chuyên dụng.',
 '高品質なディレイラベルで、専用機器を使用してエンボス加工が可能です。', 'product/hot_stamping_delayed_labels.jpg'),

-- 3️⃣ Peach-feel coating
(4, 'Peach-feel Coating', 'Phủ bề mặt cảm giác nhung mịn', 'ピーチフィールコーティング',
 'A luxurious matte surface treatment with a satiny feel.',
 'Xử lý bề mặt mờ cao cấp mang lại cảm giác mềm mại như nhung.',
 'サテンのような手触りを持つ高級感のあるマット仕上げです。', 'product/peach_feel_coating.jpg'),

-- 4️⃣ Luminist ink
(4, 'Luminist Ink', 'Mực phát sáng Luminist', 'ルミニストインク',
 'A printing technique that creates a beautiful, aurora-like luster.',
 'Công nghệ in tạo hiệu ứng ánh sáng rực rỡ giống cực quang.',
 'オーロラのような美しい輝きを生み出す印刷技術です。', 'product/luminist_ink.jpg'),

-- 5️⃣ Shrink film
(4, 'Shrink Film', 'Màng co', 'シュリンクフィルム',
 'An alternative to blister packaging, this environmentally friendly, resource-saving package makes it possible to highlight information while displaying the product.',
 'Giải pháp thay thế cho bao bì vỉ nhựa, thân thiện với môi trường và tiết kiệm tài nguyên, giúp hiển thị thông tin và sản phẩm cùng lúc.',
 'ブリスターパッケージに代わる環境に優しく資源を節約できる包装で、情報を強調しつつ製品を見せることができます。',
 'product/shrink_film.jpg'),

-- 6️⃣ Tamper-proof bottom-filled carton (patent pending)
(4, 'Tamper-proof Bottom-filled Carton (Patent Pending)',
 'Hộp carton chống giả, đóng từ đáy (đang chờ cấp bằng sáng chế)', '改ざん防止ボトム充填カートン（特許出願中）',
 'Since sets may be completed by inserting the product via the bottom of the box, the process from box assembly to sealing is streamlined.',
 'Sản phẩm có thể được đóng gói từ đáy hộp, giúp tối ưu quy trình lắp ráp và niêm phong.',
 '箱の底から製品を挿入できるため、組立から封緘までの工程が効率化されます。',
 'product/tamper_proof_bottom_filled_carton.jpg'),

-- 7️⃣ Two-Piece Carton
(4, 'Two-Piece Carton', 'Hộp hai phần', 'ツーピースカートン',
 'Created by combining paper with resin sheets, this package makes it possible to view the contents while reducing the amount of plastic used.',
 'Được tạo bằng cách kết hợp giấy và nhựa, cho phép nhìn thấy sản phẩm bên trong và giảm lượng nhựa sử dụng.',
 '紙と樹脂シートを組み合わせて作られ、内容物を見ながらプラスチック使用量を削減できます。',
 'product/two_piece_carton.jpg'),

-- 8️⃣ Package with integrated insert
(4, 'Package with Integrated Insert', 'Bao bì có phần chèn tích hợp', 'インサート一体型パッケージ',
 'Since the insert is printed directly on the package, it is not necessary to enclose it. This has the benefits of streamlining assembly work and saving resources.',
 'Phần chèn được in trực tiếp lên bao bì, giúp loại bỏ nhu cầu chèn riêng, tiết kiệm tài nguyên và giảm công đoạn lắp ráp.',
 'インサートがパッケージに直接印刷されているため、別途封入する必要がなく、作業効率と資源節約に優れています。',
 'product/package_with_integrated_insert.jpg');
