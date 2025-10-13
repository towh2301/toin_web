------- Insert Labels
INSERT INTO
    pages_product (
        type_id,
        en_title,
        vi_title,
        jp_title,
        en_description,
        vi_description,
        jp_description
    )
VALUES
    -- 1. Tack Labels
    (
        1,
        'Tack Labels',
        'Nhãn dính',
        'タックラベル',
        'High-adhesion tack labels designed for secure attachment on various surfaces. Ideal for packaging, logistics, and industrial use.',
        'Nhãn dính có độ bám dính cao, thích hợp cho nhiều bề mặt khác nhau. Phù hợp trong đóng gói, vận chuyển và công nghiệp.',
        '高い粘着力を持つタックラベルで、さまざまな表面にしっかりと貼り付けられます。包装、物流、工業用途に最適です。'
    ),

-- 2. Single-sheet Labels
(
    1,
    'Single-sheet Labels',
    'Nhãn đơn tờ',
    '単票ラベル',
    'High-quality single-sheet labels that offer flexibility and easy customization for printing. Perfect for small-batch or specialty products.',
    'Nhãn đơn tờ chất lượng cao, dễ dàng in ấn và tùy chỉnh. Thích hợp cho các sản phẩm đặc biệt hoặc số lượng nhỏ.',
    '高品質の単票ラベルで、印刷やカスタマイズが簡単です。少量生産や特別な製品に最適です。'
),

-- 3. Delayed Labels
(
    1,
    'Delayed Labels',
    'Nhãn dính trễ',
    'ディレイラベル',
    'Special delayed-adhesion labels that allow repositioning or time-delayed sticking for process flexibility.',
    'Nhãn dính trễ đặc biệt cho phép dán lại hoặc dán sau thời gian nhất định, giúp linh hoạt trong quy trình sản xuất.',
    '貼り付けを遅らせたり、位置を調整できる特殊なディレイラベルで、作業工程に柔軟性を持たせます。'
),

-- 4. Glue Labels
(
    1,
    'Glue Labels',
    'Nhãn keo dán',
    '糊付けラベル',
    'Traditional glue-applied labels with excellent durability and smooth finish, suitable for glass, plastic, and paper containers.',
    'Nhãn sử dụng keo dán truyền thống, độ bền cao và bề mặt mịn, phù hợp cho chai lọ thủy tinh, nhựa và giấy.',
    '伝統的な糊付けタイプのラベルで、高い耐久性と滑らかな仕上がりを持ち、ガラス・プラスチック・紙容器に適しています。'
),

-- 5. POP Labels
(
    1,
    'POP Labels',
    'Nhãn POP',
    'POPラベル',
    'Eye-catching POP labels designed for product promotion, shelf display, and retail marketing impact.',
    'Nhãn POP nổi bật, dùng để quảng bá sản phẩm, trưng bày trên kệ và tăng hiệu quả tiếp thị bán lẻ.',
    '店頭での販促や陳列に効果的な、視覚的に目を引くPOPラベルです。'
);

------ Insert intructions
INSERT INTO
    pages_product (
        type_id,
        en_title,
        vi_title,
        jp_title,
        en_description,
        vi_description,
        jp_description
    )
VALUES (
        2,
        'Instructions',
        'Tờ hướng dẫn',
        '説明書',
        'From pharmaceuticals (medical/OTC use) to cosmetics, we produce instructions (package inserts) based on stringent quality standards that provide consumers with accurate product information.',
        'Từ dược phẩm (dùng trong y tế/không kê đơn) đến mỹ phẩm, chúng tôi đều viết hướng dẫn (tờ hướng dẫn sử dụng) dựa trên các tiêu chuẩn chất lượng nghiêm ngặt, cung cấp cho người tiêu dùng thông tin chính xác về sản phẩm.',
        '医薬品（医療用・OTC用）から化粧品まで、消費者に正確な製品情報を提供するための厳しい品質基準に基づいた説明書（添付文書）を制作しています。'
    );

INSERT INTO
    pages_product (
        type_id,
        en_title,
        vi_title,
        jp_title,
        en_description,
        vi_description,
        jp_description,
        image
    )
VALUES
    -- 1️⃣ Crush luster
    (
        4,
        'Crush Luster',
        'Hiệu ứng ánh sáng Crush',
        'クラッシュラスター',
        'This printing technology applies three-dimensional textures that reflect light randomly.',
        'Công nghệ in này tạo ra bề mặt có hiệu ứng ba chiều, phản chiếu ánh sáng ngẫu nhiên.',
        '光をランダムに反射する立体的な質感を持つ印刷技術です。',
        'product/crush_luster.jpg'
    ),

-- 2️⃣ Hot stamping delayed labels
(
    4,
    'Hot Stamping Delayed Labels',
    'Nhãn dính trễ ép nhiệt',
    'ホットスタンピングディレイラベル',
    'These high-quality delayed labels may be embossed using specialized equipment.',
    'Nhãn dính trễ chất lượng cao có thể được ép nổi bằng thiết bị chuyên dụng.',
    '高品質なディレイラベルで、専用機器を使用してエンボス加工が可能です。',
    'product/hot_stamping_delayed_labels.jpg'
),

-- 3️⃣ Peach-feel coating
(
    4,
    'Peach-feel Coating',
    'Phủ bề mặt cảm giác nhung mịn',
    'ピーチフィールコーティング',
    'A luxurious matte surface treatment with a satiny feel.',
    'Xử lý bề mặt mờ cao cấp mang lại cảm giác mềm mại như nhung.',
    'サテンのような手触りを持つ高級感のあるマット仕上げです。',
    'product/peach_feel_coating.jpg'
),

-- 4️⃣ Luminist ink
(
    4,
    'Luminist Ink',
    'Mực phát sáng Luminist',
    'ルミニストインク',
    'A printing technique that creates a beautiful, aurora-like luster.',
    'Công nghệ in tạo hiệu ứng ánh sáng rực rỡ giống cực quang.',
    'オーロラのような美しい輝きを生み出す印刷技術です。',
    'product/luminist_ink.jpg'
),

-- 5️⃣ Shrink film
(
    4,
    'Shrink Film',
    'Màng co',
    'シュリンクフィルム',
    'An alternative to blister packaging, this environmentally friendly, resource-saving package makes it possible to highlight information while displaying the product.',
    'Giải pháp thay thế cho bao bì vỉ nhựa, thân thiện với môi trường và tiết kiệm tài nguyên, giúp hiển thị thông tin và sản phẩm cùng lúc.',
    'ブリスターパッケージに代わる環境に優しく資源を節約できる包装で、情報を強調しつつ製品を見せることができます。',
    'product/shrink_film.jpg'
),

-- 6️⃣ Tamper-proof bottom-filled carton (patent pending)
(
    4,
    'Tamper-proof Bottom-filled Carton (Patent Pending)',
    'Hộp carton chống giả, đóng từ đáy (đang chờ cấp bằng sáng chế)',
    '改ざん防止ボトム充填カートン（特許出願中）',
    'Since sets may be completed by inserting the product via the bottom of the box, the process from box assembly to sealing is streamlined.',
    'Sản phẩm có thể được đóng gói từ đáy hộp, giúp tối ưu quy trình lắp ráp và niêm phong.',
    '箱の底から製品を挿入できるため、組立から封緘までの工程が効率化されます。',
    'product/tamper_proof_bottom_filled_carton.jpg'
),

-- 7️⃣ Two-Piece Carton
(
    4,
    'Two-Piece Carton',
    'Hộp hai phần',
    'ツーピースカートン',
    'Created by combining paper with resin sheets, this package makes it possible to view the contents while reducing the amount of plastic used.',
    'Được tạo bằng cách kết hợp giấy và nhựa, cho phép nhìn thấy sản phẩm bên trong và giảm lượng nhựa sử dụng.',
    '紙と樹脂シートを組み合わせて作られ、内容物を見ながらプラスチック使用量を削減できます。',
    'product/two_piece_carton.jpg'
),

-- 8️⃣ Package with integrated insert
(
    4,
    'Package with Integrated Insert',
    'Bao bì có phần chèn tích hợp',
    'インサート一体型パッケージ',
    'Since the insert is printed directly on the package, it is not necessary to enclose it. This has the benefits of streamlining assembly work and saving resources.',
    'Phần chèn được in trực tiếp lên bao bì, giúp loại bỏ nhu cầu chèn riêng, tiết kiệm tài nguyên và giảm công đoạn lắp ráp.',
    'インサートがパッケージに直接印刷されているため、別途封入する必要がなく、作業効率と資源節約に優れています。',
    'product/package_with_integrated_insert.jpg'
);

INSERT INTO
    pages_partner (
        en_name,
        vi_name,
        jp_name,
        en_description,
        vi_description,
        jp_description,
        en_address,
        vi_address,
        jp_address,
        image
    )
VALUES (
        'TOIN VIETNAM',
        'TOIN VIỆT NAM',
        'TOINベトナム',
        'Established in Vietnam in 2013 (Manufacturing and sales company) With the aim of supporting customers'' expansion into Southeast Asia, we established a manufacturing base in the suburbs of Ho Chi Minh City, Vietnam, in 2013. Focusing on packages for cosmetics and pharmaceuticals with high added value, this production plant meets customers'' needs in a GMP-oriented environment.',
        'Được thành lập tại Việt Nam vào năm 2013 (Công ty sản xuất và kinh doanh) Nhằm hỗ trợ khách hàng mở rộng vào Đông Nam Á, chúng tôi đã thiết lập một cơ sở sản xuất tại ngoại ô Thành phố Hồ Chí Minh, Việt Nam, vào năm 2013. Tập trung vào các bao bì cho mỹ phẩm và dược phẩm có giá trị gia tăng cao, nhà máy sản xuất này đáp ứng nhu cầu của khách hàng trong môi trường định hướng GMP.',
        '2013年にベトナムで設立（製造および販売会社）東南アジアへの顧客の事業拡大を支援することを目指し、2013年にベトナムのホーチミン市郊外に製造拠点を設立しました。化粧品や医薬品向けの高付加価値パッケージに注力し、この生産工場はGMP指向の環境でお客様のニーズに応えます。',
        'Lot B_1C_CN, Road DE4 & NE4A, My Phuoc 3 Industrial Park, Chanh Phu Hoa ward, Ho Chi Minh City, Vietnam',
        'Lô B_1C_CN, Đường DE4 & NE4A, Khu Công Nghiệp Mỹ Phước 3, Phường Chánh Phú Hòa, Thành phố Hồ Chí Minh, Việt Nam',
        'ベトナム、ホーチミン市、チャンフーホア区、ミーフォック3工業団地、DE4およびNE4A道路、B_1C_CN区画',
        NULL
    ),
    (
        'TOIN THAILAND',
        'TOIN THÁI LAN',
        'TOINタイランド',
        'Established in Thailand in 2008 (Sales company) With the aim of serving as a bridge between customers in Japan and customer''s production bases in Southeast Asia, we established this business in Bangkok, Thailand, to handle commercial functions. Forming capital alliances with leading local manufacturers, it globally procures and distributes a wide range of packaging materials, from packages to labels.',
        'Được thành lập tại Thái Lan vào năm 2008 (Công ty kinh doanh) Nhằm làm cầu nối giữa khách hàng tại Nhật Bản và các cơ sở sản xuất của khách hàng tại Đông Nam Á, chúng tôi đã thành lập doanh nghiệp này tại Bangkok, Thái Lan, để xử lý các chức năng thương mại. Hình thành các liên minh vốn với các nhà sản xuất địa phương hàng đầu, công ty này cung ứng và phân phối toàn cầu nhiều loại vật liệu đóng gói, từ bao bì đến nhãn mác.',
        '2008年にタイで設立（販売会社）日本のお客様と東南アジアの生産拠点をつなぐ架け橋となることを目指し、タイのバンコクにこの事業を設立し、商業機能を担当しています。主要な地元メーカーと資本提携を結び、パッケージからラベルまで幅広い包装材料をグローバルに調達・流通しています。',
        'PANJATHANI TOWER, Floor 12th 127/14 Nonsee Rd., Chongnonsee, Yannawa, Bangkok 10120 Thailand',
        'Tòa PANJATHANI, Tầng 12, 127/14 Đường Nonsee, Chongnonsee, Yannawa, Bangkok 10120, Thái Lan',
        'タイ、バンコク10120、ヤンナワー、チョンノンシー、ノンシー通り127/14、パンジャタニタワー12階',
        NULL
    ),
    (
        'Overseas Material Procurement',
        'Thu Mua Vật Liệu Nước Ngoài',
        '海外資材調達',
        'Printing Solution Co., Ltd. (Bangkok Thailand) In order to meet customers'' needs for international materials procurement and to supply materials to local corporations, we acquired a 30% share in Printing Solution Co., Ltd. (PSC), a printing and paper products company in Bangkok, Thailand. We provide guidance on processing technologies and outsource manufacturing commissions to them. The company is one of Thailand''s leading manufacturers focused on producing cosmetics packages. It is notably able to supply plastic-based packages (PP, PET) whose quality is equivalent to products manufactured in Japan.',
        'Công ty TNHH Giải pháp In ấn (Bangkok, Thái Lan) Nhằm đáp ứng nhu cầu thu mua vật liệu quốc tế của khách hàng và cung cấp vật liệu cho các tập đoàn địa phương, chúng tôi đã mua 30% cổ phần của Công ty TNHH Giải pháp In ấn (PSC), một công ty in ấn và sản phẩm giấy tại Bangkok, Thái Lan. Chúng tôi cung cấp hướng dẫn về công nghệ chế biến và ủy thác sản xuất cho họ. Công ty này là một trong những nhà sản xuất hàng đầu tại Thái Lan, tập trung vào sản xuất bao bì mỹ phẩm. Đặc biệt, công ty có khả năng cung cấp các bao bì dựa trên nhựa (PP, PET) có chất lượng tương đương với các sản phẩm được sản xuất tại Nhật Bản.',
        'プリンティング・ソリューション株式会社（タイ、バンコク）お客様の国際的な資材調達ニーズに応え、地元企業への資材供給を行うため、タイのバンコクにある印刷および紙製品会社であるプリンティング・ソリューション株式会社（PSC）の30％の株式を取得しました。加工技術に関する指導を提供し、製造業務を委託しています。この会社は、化粧品パッケージの生産に注力するタイを代表するメーカーの一つであり、特に日本で製造された製品と同等の品質のプラスチックベースのパッケージ（PP、PET）を供給することができます。',
        NULL,
        NULL,
        NULL,
        NULL
    ),
    (
        'Other',
        'Khác',
        'その他',
        'We procure and supply high-quality printed package materials to customers globally, focusing on bases in countries in Southeast Asia. This includes a wide range of materials, such as processed paper (metallized paper, etc.), bottles/tubes, soft packaging, and shrink film mounting.',
        'Chúng tôi thu mua và cung cấp vật liệu bao bì in ấn chất lượng cao cho khách hàng trên toàn cầu, tập trung vào các cơ sở tại các quốc gia Đông Nam Á. Điều này bao gồm nhiều loại vật liệu, như giấy đã qua xử lý (giấy kim loại, v.v.), chai/lọ, bao bì mềm và màng co.',
        '東南アジア諸国の拠点を中心に、世界中のお客様に高品質な印刷包装材料を調達・供給しています。これには、加工紙（金属紙など）、ボトル/チューブ、ソフトパッケージ、シュリンクフィルムなど幅広い材料が含まれます。',
        NULL,
        NULL,
        NULL,
        NULL
    );