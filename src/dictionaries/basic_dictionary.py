"""
基本辞書データ
Phase P-1-1: 最小限実装（「クロード」→「Claude」のみ）
"""

BASIC_DICTIONARY = {
# AI関連
    "クロード": "Claude",
    "くろーど": "Claude",
    "クローディア": "Claude",
    
    "クロードコード": "Claude Code",
    "くろーどこーど": "Claude Code",
    
    "チャットジーピーティー": "ChatGPT",
    "ちゃっとじーぴーてぃー": "ChatGPT",
    "チャットGPT": "ChatGPT",
    "ちゃっとGPT": "ChatGPT",
    
    "ジェミニ": "Gemini",
    "じぇみに": "Gemini",
    "ジェミナイ": "Gemini",
    
    "ジェミニシーエルアイ": "Gemini CLI",
    "じぇみにしーえるあい": "Gemini CLI",
    "ジェミナイシーエルアイ": "Gemini CLI",
    "ジェミナイしーえるあい": "Gemini CLI",
    
    "パープレキシティー": "Perplexity",
    "ぱーぷれくしてぃー": "Perplexity",
    "パープレックス": "Perplexity",
    
    "ジェンスパーク": "Genspark",
    "じぇんすぱーく": "Genspark",
    
    "グロック": "Grok",
    "ぐろっく": "Grok",
    "グロッグ": "Grok",
    
    "ディファイ": "Dify",
    "でぃふぁい": "Dify",
    "ディフィー": "Dify",
    
    "カーソル": "Cursor",
    "かーそる": "Cursor",
    
    "ボルト": "Bolt",
    "ぼると": "Bolt",
    
    "レプリット": "Replit",
    "れぷりっと": "Replit",
    
    "ミッドジャーニー": "Midjourney",
    "みっどじゃーにー": "Midjourney",
    
    "ダリー": "DALL-E",
    "だりー": "DALL-E",
    "ダリツー": "DALL-E 2",
    "ダリスリー": "DALL-E 3",
    
    "ステーブルディフュージョン": "Stable Diffusion",
    "すてーぶるでぃふゅーじょん": "Stable Diffusion",
    
    "ランウェイ": "Runway",
    "らんうぇい": "Runway",
    
    "ギットハブコパイロット": "GitHub Copilot",
    "ぎっとはぶこぱいろっと": "GitHub Copilot",
    "コパイロット": "Copilot",
    "こぱいろっと": "Copilot",
    
    "コードウィスパラー": "CodeWhisperer",
    "こーどうぃすぱらー": "CodeWhisperer",
    
    "タブナイン": "Tabnine",
    "たぶないん": "Tabnine",
    
    "ジャスパー": "Jasper",
    "じゃすぱー": "Jasper",
    
    "ハギングフェイス": "Hugging Face",
    "はぎんぐふぇいす": "Hugging Face",
    
    "ラングチェーン": "LangChain",
    "らんぐちぇーん": "LangChain",
    
    "ピンコーン": "Pinecone",
    "ぴんこーん": "Pinecone",
    
    "オープンエーアイ": "OpenAI",
    "おーぷんえーあい": "OpenAI",
    
    "アンソロピック": "Anthropic",
    "あんそろぴっく": "Anthropic",
    
    "ウィスパー": "Whisper",
    "うぃすぱー": "Whisper",
    
    "エムシーピー": "MCP",
    "えむしーぴー": "MCP",
    "えむしぃぴー": "MCP",
    
    "えるえるえむ": "LLM",
    "エルエルエム": "LLM",
    
    "エージーアイ": "AGI",
    "えーじーあい": "AGI",
    "エイジーアイ": "AGI",

    # 技術系 / 言語・フレームワーク
    "エッチティーエムエル": "HTML",
    "えっちてぃーえむえる": "HTML",
    "エッチティーエムエルファイブ": "HTML5",

    "シーエスエス": "CSS",
    "しーえすえす": "CSS",
    "シーエスエススリー": "CSS3",

    "エスキューエル": "SQL",
    "えすきゅーえる": "SQL",
    "シークエル": "SQL",

    "ジェイソン": "JSON",
    "じぇいそん": "JSON",

    "エックスエムエル": "XML",
    "えっくすえむえる": "XML",

    "ジャバ": "Java",
    "じゃば": "Java",
    "ジャヴァ": "Java",

    "パイソン": "Python",
    "ぱいそん": "Python",
    "パイトン": "Python",

    "ジャバスクリプト": "JavaScript",
    "じゃばすくりぷと": "JavaScript",
    "ジェイエス": "JS",
    "じぇいえす": "JS",

    "タイプスクリプト": "TypeScript",
    "たいぷすくりぷと": "TypeScript",
    "ティーエス": "TS",
    "てぃーえす": "TS",

    "リアクト": "React",
    "りあくと": "React",
    "リアクトジェイエス": "React.js",

    "アンギュラー": "Angular",
    "あんぎゅらー": "Angular",

    "ノード": "Node.js",
    "のーど": "Node.js",
    "ノードジェイエス": "Node.js",

    "エクスプレス": "Express",
    "えくすぷれす": "Express",
    "エクスプレスジェイエス": "Express.js",

    "ネクスト": "Next.js",
    "ねくすと": "Next.js",
    "ネクストジェイエス": "Next.js",

    "ニュークスト": "Nuxt.js",
    "にゅーくすと": "Nuxt.js",
    "ニュークストジェイエス": "Nuxt.js",

    "スベルト": "Svelte",
    "すべると": "Svelte",

    "ファストエーピーアイ": "FastAPI",
    "ふぁすとえーぴーあい": "FastAPI",

    "ジャンゴ": "Django",
    "じゃんご": "Django",

    "フラスク": "Flask",
    "ふらすく": "Flask",

    "ルビー": "Ruby",
    "るびー": "Ruby",
    "ルビーオンレイルズ": "Ruby on Rails",

    "ピーエッチピー": "PHP",
    "ぴーえっちぴー": "PHP",

    "ララベル": "Laravel",
    "らればる": "Laravel",

    "シーシャープ": "C#",
    "しーしゃーぷ": "C#",
    "シープラスプラス": "C++",

    "コトリン": "Kotlin",
    "ことりん": "Kotlin",

    "スイフト": "Swift",
    "すいふと": "Swift",

    "フラッター": "Flutter",
    "ふらったー": "Flutter",

    "リアクトネイティブ": "React Native",
    "りあくとねいてぃぶ": "React Native",

    "イオニック": "Ionic",
    "いおにっく": "Ionic",

    "コルドバ": "Cordova",
    "こるどば": "Cordova",

    "ザマリン": "Xamarin",
    "ざまりん": "Xamarin",

    "ユニティ": "Unity",
    "ゆにてぃ": "Unity",

    "アンリアル": "Unreal Engine",
    "あんりある": "Unreal Engine",
    "アンリアルエンジン": "Unreal Engine",

    "ブートストラップ": "Bootstrap",
    "ぶーとすとらっぷ": "Bootstrap",

    "テイルウィンド": "Tailwind CSS",
    "ているうぃんど": "Tailwind CSS",
    "テイルウィンドシーエスエス": "Tailwind CSS",

    "ウェブパック": "Webpack",
    "うぇぶぱっく": "Webpack",

    "パーセル": "Parcel",
    "ぱーせる": "Parcel",

    "ガルプ": "Gulp",
    "がるぷ": "Gulp",

    "グラント": "Grunt",
    "ぐらんと": "Grunt",

    "バベル": "Babel",
    "ばべる": "Babel",

    "エスリント": "ESLint",
    "えすりんと": "ESLint",

    "プリティア": "Prettier",
    "ぷりてぃあ": "Prettier",

    "ジェスト": "Jest",
    "じぇすと": "Jest",

    "サイプレス": "Cypress",
    "さいぷれす": "Cypress",

    "プレイライト": "Playwright",
    "ぷれいらいと": "Playwright",

    "ストーリーブック": "Storybook",
    "すとーりーぶっく": "Storybook",

    # 技術系 / コード構文・命令
    "デフ": "def",
    "でふ": "def",

    "クラス": "class",
    "くらす": "class",

    "ファンクション": "function",
    "ふぁんくしょん": "function",

    "インポート": "import",
    "いんぽーと": "import",

    "フロム": "from",
    "ふろむ": "from",

    "リターン": "return",
    "りたーん": "return",

    "エルス": "else",
    "えるす": "else",

    "エルスイフ": "else if",
    "えるすいふ": "else if",
    "エルシフ": "elif",

    "ワイル": "while",
    "わいる": "while",

    "ブレイク": "break",
    "ぶれいく": "break",

    "コンティニュー": "continue",
    "こんてぃにゅー": "continue",

    "エクセプト": "except",
    "えくせぷと": "except",

    "ファイナリー": "finally",
    "ふぁいなりー": "finally",

    "レイズ": "raise",
    "れいず": "raise",

    "でぷろい": "デプロイ",
    "ディプロい": "デプロイ",

    "セルフ": "self",
    "せるふ": "self",

    "スーパー": "super",
    "すーぱー": "super",

    "アンディファインド": "undefined",
    "あんでぃふぁいんど": "undefined",

    "トゥルー": "true",
    "とぅるー": "true",

    "フォルス": "false",
    "ふぉるす": "false",

    "コンスト": "const",
    "こんすと": "const",

    "ラムダ": "lambda",
    "らむだ": "lambda",

    "フィルター": "filter",
    "ふぃるたー": "filter",

    "リデュース": "reduce",
    "りでゅーす": "reduce",

    "フォーイーチ": "forEach",
    "ふぉーいーち": "forEach",

    "レングス": "length",
    "れんぐす": "length",

    "スプライス": "splice",
    "すぷらいす": "splice",

    "スライス": "slice",
    "すらいす": "slice",

    "ジョイン": "join",
    "じょいん": "join",

    "スプリット": "split",
    "すぷりっと": "split",

    "リプレイス": "replace",
    "りぷれいす": "replace",

    "インクルーズ": "includes",
    "いんくるーず": "includes",

    "インデックスオブ": "indexOf",
    "いんでっくすおぶ": "indexOf",

    "バリューズ": "values",
    "ばりゅーず": "values",

    "エントリーズ": "entries",
    "えんとりーず": "entries",

    "アサイン": "assign",
    "あさいん": "assign",

    "スプレッド": "spread",
    "すぷれっど": "spread",

    "デストラクチャリング": "destructuring",
    "ですとらくちゃりんぐ": "destructuring",

    "アシンク": "async",
    "あしんく": "async",

    "アウェイト": "await",
    "あうぇいと": "await",

    "プロミス": "Promise",
    "ぷろみす": "Promise",

    "コールバック": "callback",
    "こーるばっく": "callback",

    "クロージャー": "closure",
    "くろーじゃー": "closure",

    "ホイスティング": "hoisting",
    "ほいすてぃんぐ": "hoisting",

    "プロトタイプ": "prototype",
    "ぷろとたいぷ": "prototype",

    "インヘリタンス": "inheritance",
    "いんへりたんす": "inheritance",

    "ポリモーフィズム": "polymorphism",
    "ぽりもーふぃずむ": "polymorphism",

    "エンカプスレーション": "encapsulation",
    "えんかぷすれーしょん": "encapsulation",

    "アブストラクション": "abstraction",
    "あぶすとらくしょん": "abstraction",

    # 技術系 / 開発ツール
    "ギット": "Git",
    "ぎっと": "Git",

    "ギットハブ": "GitHub",
    "ぎっとはぶ": "GitHub",

    "ギットラブ": "GitLab",
    "ぎっとらぶ": "GitLab",

    "ビットバケット": "Bitbucket",
    "びっとばけっと": "Bitbucket",

    "ブイエスコード": "VS Code",
    "ぶいえすこーど": "VS Code",

    "ビジュアルスタジオ": "Visual Studio",
    "びじゅあるすたじお": "Visual Studio",

    "ビジュアルスタジオコード": "Visual Studio Code",
    "びじゅあるすたじおこーど": "Visual Studio Code",

    "サブライムテキスト": "Sublime Text",
    "さぶらいむてきすと": "Sublime Text",

    "インテリジェイ": "IntelliJ IDEA",
    "いんてりじぇい": "IntelliJ IDEA",

    "ウェブストーム": "WebStorm",
    "うぇぶすとーむ": "WebStorm",

    "パイチャーム": "PyCharm",
    "ぱいちゃーむ": "PyCharm",

    "エクリプス": "Eclipse",
    "えくりぷす": "Eclipse",

    "ネットビーンズ": "NetBeans",
    "ねっとびーんず": "NetBeans",

    "エックスコード": "Xcode",
    "えっくすこーど": "Xcode",

    "アンドロイドスタジオ": "Android Studio",
    "あんどろいどすたじお": "Android Studio",

    "ドッカー": "Docker",
    "どっかー": "Docker",

    "ドッカーコンポーズ": "Docker Compose",
    "どっかーこんぽーず": "Docker Compose",

    "キューバーネティス": "Kubernetes",
    "きゅーばーねてぃす": "Kubernetes",

    "キューバーネテス": "Kubernetes",
    "きゅーばーねてす": "Kubernetes",

    "ケーエイトエス": "K8s",
    "けーえいとえす": "K8s",

    "ジェンキンス": "Jenkins",
    "じぇんきんす": "Jenkins",

    "ギットハブアクションズ": "GitHub Actions",
    "ぎっとはぶあくしょんず": "GitHub Actions",

    "サークルシーアイ": "CircleCI",
    "さーくるしーあい": "CircleCI",

    "トラビスシーアイ": "Travis CI",
    "とらびすしーあい": "Travis CI",

    "コンフルエンス": "Confluence",
    "こんふるえんす": "Confluence",

    "トレロ": "Trello",
    "とれろ": "Trello",

    "アサナ": "Asana",
    "あさな": "Asana",

    "スラック": "Slack",
    "すらっく": "Slack",

    "ディスコード": "Discord",
    "でぃすこーど": "Discord",

    "マイクロソフトチームズ": "Microsoft Teams",
    "まいくろそふとちーむず": "Microsoft Teams",

    "チームズ": "Teams",
    "ちーむず": "Teams",

    "ズーム": "Zoom",
    "ずーむ": "Zoom",

    "ポストマン": "Postman",
    "ぽすとまん": "Postman",

    "インソムニア": "Insomnia",
    "いんそむにあ": "Insomnia",

    "ファイアーベース": "Firebase",
    "ふぁいあーべーす": "Firebase",

    "スパベース": "Supabase",
    "すぱべーす": "Supabase",

    "ネットリファイ": "Netlify",
    "ねっとりふぁい": "Netlify",

    "バーセル": "Vercel",
    "ばーせる": "Vercel",

    "ヘロク": "Heroku",
    "へろく": "Heroku",

    "ディジタルオーシャン": "DigitalOcean",
    "でぃじたるおーしゃん": "DigitalOcean",

    "リノード": "Linode",
    "りのーど": "Linode",

    "バルチャー": "Vultr",
    "ばるちゃー": "Vultr",

    "テラフォーム": "Terraform",
    "てらふぉーむ": "Terraform",

    "アンシブル": "Ansible",
    "あんしぶる": "Ansible",

    "ベイグラント": "Vagrant",
    "べいぐらんと": "Vagrant",

    "ノード": "Node.js",
    "のーど": "Node.js",

    "エヌピーエム": "npm",
    "えぬぴーえむ": "npm",

    "コンダ": "conda",
    "こんだ": "conda",

    "アナコンダ": "Anaconda",
    "あなこんだ": "Anaconda",

    "ミニコンダ": "Miniconda",
    "みにこんだ": "Miniconda",

    "ホームブリュー": "Homebrew",
    "ほーむぶりゅー": "Homebrew",

    "チョコレイティ": "Chocolatey",
    "ちょこれいてぃ": "Chocolatey",

    "アパッチ": "Apache",
    "あぱっち": "Apache",

    "エンジンエックス": "Nginx",
    "えんじんえっくす": "Nginx",

    "レディス": "Redis",
    "れでぃす": "Redis",

    "イーエスリント": "ESLint",
    "いーえすりんと": "ESLint",

    "プリティア": "Prettier",
    "ぷりてぃあ": "Prettier",

    "リントステージド": "lint-staged",
    "りんとすてーじど": "lint-staged",

    "ロールアップ": "Rollup",
    "ろーるあっぷ": "Rollup",

    "パーセル": "Parcel",
    "ぱーせる": "Parcel",

    "スノーパック": "Snowpack",
    "すのーぱっく": "Snowpack",

    "ターボパック": "Turbopack",
    "たーぼぱっく": "Turbopack",

    "フィグマ": "Figma",
    "ふぃぐま": "Figma",

    "スケッチ": "Sketch",
    "すけっち": "Sketch",

    "アドビエックスディー": "Adobe XD",
    "あどびえっくすでぃー": "Adobe XD",

    "インビジョン": "InVision",
    "いんびじょん": "InVision",

    "ゼプリン": "Zeplin",
    "ぜぷりん": "Zeplin",

    "ストーリーブック": "Storybook",
    "すとーりーぶっく": "Storybook",

     # Adobe系・クリエイティブツール
    "フォトショップ": "Photoshop",
    "ふぉとしょっぷ": "Photoshop",

    "イラストレーター": "Illustrator",
    "いらすとれーたー": "Illustrator",

    "プレミア": "Premiere Pro",
    "ぷれみあ": "Premiere Pro",
    "プレミアプロ": "Premiere Pro",

    "アフターエフェクツ": "After Effects",
    "あふたーえふぇくつ": "After Effects",

    "ライトルーム": "Lightroom",
    "らいとるーむ": "Lightroom",

    "インデザイン": "InDesign",
    "いんでざいん": "InDesign",

    "ドリームウィーバー": "Dreamweaver",
    "どりーむうぃーばー": "Dreamweaver",

    "プレリュード": "Prelude",
    "ぷれりゅーど": "Prelude",

    "エンコア": "Encore",
    "えんこあ": "Encore",

    "ブリッジ": "Bridge",
    "ぶりっじ": "Bridge",

    "カメラロー": "Camera Raw",
    "かめらろー": "Camera Raw",

    "ディメンション": "Dimension",
    "でぃめんしょん": "Dimension",

    "キャラクターアニメーター": "Character Animator",
    "きゃらくたーあにめーたー": "Character Animator",

    "プレミアラッシュ": "Premiere Rush",
    "ぷれみあらっしゅ": "Premiere Rush",

    "スパーク": "Spark",
    "すぱーく": "Spark",

    "クリエイティブクラウド": "Creative Cloud",
    "くりえいてぃぶくらうど": "Creative Cloud",

    # 他のクリエイティブツール
    "ブレンダー": "Blender",
    "ぶれんだー": "Blender",

     # 技術系 / クラウドサービス
    "エーダブリューエス": "AWS",
    "えーだぶりゅーえす": "AWS",
    "アマゾンウェブサービス": "Amazon Web Services",

    "アジュール": "Azure",
    "あじゅーる": "Azure",
    "マイクロソフトアジュール": "Microsoft Azure",

    "ジーシーピー": "GCP",
    "じーしーぴー": "GCP",
    "グーグルクラウドプラットフォーム": "Google Cloud Platform",

    "グーグルクラウド": "Google Cloud",
    "ぐーぐるくらうど": "Google Cloud",

    "ファイアーベース": "Firebase",
    "ふぁいあーべーす": "Firebase",

    "スパベース": "Supabase",
    "すぱべーす": "Supabase",

    "ヘロク": "Heroku",
    "へろく": "Heroku",

    "ネットリファイ": "Netlify",
    "ねっとりふぁい": "Netlify",

    "バーセル": "Vercel",
    "ばーせる": "Vercel",

    "ディジタルオーシャン": "DigitalOcean",
    "でぃじたるおーしゃん": "DigitalOcean",

    "リノード": "Linode",
    "りのーど": "Linode",

    "バルチャー": "Vultr",
    "ばるちゃー": "Vultr",

    "クラウドフレア": "Cloudflare",
    "くらうどふれあ": "Cloudflare",

    "アカマイ": "Akamai",
    "あかまい": "Akamai",

    # ビジネス系 / ビジネスツール
    "スラック": "Slack",
    "すらっく": "Slack",

    "チームズ": "Teams",
    "ちーむず": "Teams",
    "マイクロソフトチームズ": "Microsoft Teams",

    "ズーム": "Zoom",
    "ずーむ": "Zoom",

    "グーグルミート": "Google Meet",
    "ぐーぐるみーと": "Google Meet",

    "スカイプ": "Skype",
    "すかいぷ": "Skype",

    "ディスコード": "Discord",
    "でぃすこーど": "Discord",

    "ノーション": "Notion",
    "のーしょん": "Notion",

    "オブシディアン": "Obsidian",
    "おぶしでぃあん": "Obsidian",

    "エバーノート": "Evernote",
    "えばーのーと": "Evernote",

    "ワンノート": "OneNote",
    "わんのーと": "OneNote",

    "グーグルドライブ": "Google Drive",
    "ぐーぐるどらいぶ": "Google Drive",

    "ドロップボックス": "Dropbox",
    "どろっぷぼっくす": "Dropbox",

    "ワンドライブ": "OneDrive",
    "わんどらいぶ": "OneDrive",


    "セールスフォース": "Salesforce",
    "せーるすふぉーす": "Salesforce",

    "ハブスポット": "HubSpot",
    "はぶすぽっと": "HubSpot",

    "ゼンデスク": "Zendesk",
    "ぜんですく": "Zendesk",

    "グーグルアナリティクス": "Google Analytics",
    "ぐーぐるあなりてぃくす": "Google Analytics",

    "グーグルアド": "Google Ads",
    "ぐーぐるあど": "Google Ads",

    "グーグルアドセンス": "Google AdSense",
    "ぐーぐるあどせんす": "Google AdSense",

    "フェイスブックアド": "Facebook Ads",
    "ふぇいすぶっくあど": "Facebook Ads",

    "インスタグラムアド": "Instagram Ads",
    "いんすたぐらむあど": "Instagram Ads",

    "ユーチューブアド": "YouTube Ads",
    "ゆーちゅーぶあど": "YouTube Ads",

    "カンバ": "Canva",
    "かんば": "Canva",
    "キャンバ": "Canva",  
    "きゃんば": "Canva",  

    "フィグマ": "Figma",
    "ふぃぐま": "Figma",

    "ドックサイン": "DocuSign",
    "どっくさいん": "DocuSign",

    "アドビクリエイティブクラウド": "Adobe Creative Cloud",
    "あどびくりえいてぃぶくらうど": "Adobe Creative Cloud",

    "カレンドリー": "Calendly",
    "かれんどりー": "Calendly",

    "バフファー": "Buffer",
    "ばふふぁー": "Buffer",
    "バッファー": "Buffer",  
    "ばっふぁー": "Buffer", 

    "フートスイート": "Hootsuite",
    "ふーとすいーと": "Hootsuite",

    "メールチンプ": "Mailchimp",
    "めーるちんぷ": "Mailchimp",

    "ショピファイ": "Shopify",
    "しょぴふぁい": "Shopify",

    "ウーコマース": "WooCommerce",
    "うーこまーす": "WooCommerce",

    "ワードプレス": "WordPress",
    "わーどぷれす": "WordPress",

    "スクエア": "Square",
    "すくえあ": "Square",

    "ペイパル": "PayPal",
    "ぺいぱる": "PayPal",

    "ストライプ": "Stripe",
    "すとらいぷ": "Stripe",

    "アマゾンウェブサービス": "AWS",
    "あまぞんうぇぶさーびす": "AWS",

    "エーダブリューエス": "AWS",
    "えーだぶりゅーえす": "AWS",

    "ギットハブ": "GitHub",
    "ぎっとはぶ": "GitHub",

    "ブイエスコード": "VS Code",
    "ぶいえすこーど": "VS Code",

    "ジーメール": "Gmail",
    "じーめーる": "Gmail",

    "アウトルック": "Outlook",
    "あうとるっく": "Outlook",

    "エクセル": "Excel",
    "えくせる": "Excel",

    "パワーポイント": "PowerPoint",
    "ぱわーぽいんと": "PowerPoint",

    "ワード": "Word",
    "わーど": "Word",

    "グーグルドクス": "Google Docs",
    "ぐーぐるどくす": "Google Docs",

    "グーグルスプレッドシート": "Google Sheets",
    "ぐーぐるすぷれっどしーと": "Google Sheets",

    "グーグルスライド": "Google Slides",
    "ぐーぐるすらいど": "Google Slides",

    "エアテーブル": "Airtable",
    "えあてーぶる": "Airtable",

    "ザピア": "Zapier",
    "ざぴあ": "Zapier",

    "マネーフォワード": "MoneyForward",
    "まねーふぉわーど": "MoneyForward",

    "サイボウズ": "Cybozu",
    "さいぼうず": "Cybozu",

    "チャットワーク": "Chatwork",
    "ちゃっとわーく": "Chatwork",

    "キントーン": "kintone",
    "きんとーん": "kintone",

    "ゾーホー": "Zoho",
    "ぞーほー": "Zoho",

    # ビジネス系 / コミュニケーション関連
    "スラック": "Slack",
    "すらっく": "Slack",

    "チームズ": "Teams",
    "ちーむず": "Teams",
    "ちーむす": "Teams",
    "マイクロソフトチームズ": "Microsoft Teams",

    "ズーム": "Zoom",
    "ずーむ": "Zoom",

    "グーグルミート": "Google Meet",
    "ぐーぐるみーと": "Google Meet",

    "スカイプ": "Skype",
    "すかいぷ": "Skype",

    "ディスコード": "Discord",
    "でぃすこーど": "Discord",

    "インスタグラム": "Instagram",
    "いんすたぐらむ": "Instagram",
    "インスタ": "Instagram",
    "いんすた": "Instagram",

    "ツイッター": "Twitter",
    "ついったー": "Twitter",
    "エックス": "X",
    "えっくす": "X",

    "フェイスブック": "Facebook",
    "ふぇいすぶっく": "Facebook",

    "リンクトイン": "LinkedIn",
    "りんくといん": "LinkedIn",

    "ティックトック": "TikTok",
    "てぃっくとっく": "TikTok",

    "ユーチューブ": "YouTube",
    "ゆーちゅーぶ": "YouTube",

    "スナップチャット": "Snapchat",
    "すなっぷちゃっと": "Snapchat",

    "ピンタレスト": "Pinterest",
    "ぴんたれすと": "Pinterest",

    "レディット": "Reddit",
    "れでぃっと": "Reddit",

    "ライン": "LINE",
    "らいん": "LINE",

    "ワッツアップ": "WhatsApp",
    "わっつあっぷ": "WhatsApp",

    "テレグラム": "Telegram",
    "てれぐらむ": "Telegram",

    "ウィーチャット": "WeChat",
    "うぃーちゃっと": "WeChat",

    "バイバー": "Viber",
    "ばいばー": "Viber",

    "ツイッチ": "Twitch",
    "ついっち": "Twitch",

    "クラブハウス": "Clubhouse",
    "くらぶはうす": "Clubhouse",

    "チャットワーク": "Chatwork",
    "ちゃっとわーく": "Chatwork",

    "サイボウズ": "Cybozu",
    "さいぼうず": "Cybozu",

    "ウィーボー": "Weibo",
    "うぃーぼー": "Weibo",

    "カカオトーク": "KakaoTalk",
    "かかおとーく": "KakaoTalk",

    # ビジネス系 / 企業名
    "グーグル": "Google",
    "ぐーぐる": "Google",

    "マイクロソフト": "Microsoft",
    "まいくろそふと": "Microsoft",

    "アマゾン": "Amazon",
    "あまぞん": "Amazon",

    "アップル": "Apple",
    "あっぷる": "Apple",

    "ネットフリックス": "Netflix",
    "ねっとふりっくす": "Netflix",

    "ウーバー": "Uber",
    "うーばー": "Uber",

    "エアビーアンドビー": "Airbnb",
    "えあびーあんどびー": "Airbnb",
    "えあびー": "Airbnb",

    "スポティファイ": "Spotify",
    "すぽてぃふぁい": "Spotify",

    "ツイッター": "Twitter",
    "ついったー": "Twitter",

    "セールスフォース": "Salesforce",
    "せーるすふぉーす": "Salesforce",

    "オラクル": "Oracle",
    "おらくる": "Oracle",

    "インテル": "Intel",
    "いんてる": "Intel",

    "エヌビディア": "NVIDIA",
    "えぬびでぃあ": "NVIDIA",

    "IBM": "IBM",
    "アイビーエム": "IBM",
    "あいびーえむ": "IBM",

    "アドビ": "Adobe",
    "あどび": "Adobe",

    "ズーム": "Zoom",
    "ずーむ": "Zoom",

    "スラック": "Slack",
    "すらっく": "Slack",

    "ドロップボックス": "Dropbox",
    "どろっぷぼっくす": "Dropbox",

    "ペイパル": "PayPal",
    "ぺいぱる": "PayPal",

    "楽天": "楽天",
    "らくてん": "楽天",

    "ソフトバンク": "SoftBank",
    "そふとばんく": "SoftBank",

    "ヤフー": "Yahoo",
    "やふー": "Yahoo",

    "ドコモ": "DoCoMo",
    "どこも": "DoCoMo",

    "KDDI": "KDDI",
    "ケーディーディーアイ": "KDDI",
    "けーでぃーでぃーあい": "KDDI",

    "オープンエーアイ": "OpenAI",
    "おーぷんえーあい": "OpenAI",

    "アンソロピック": "Anthropic",
    "あんそろぴっく": "Anthropic",

    "ディープマインド": "DeepMind",
    "でぃーぷまいんど": "DeepMind",

    "オープンエーアイ": "OpenAI",
    "おーぷんえーあい": "OpenAI",

    "スタビリティエーアイ": "Stability AI",
    "すたびりてぃえーあい": "Stability AI",

    "ミッドジャーニー": "Midjourney",
    "みっどじゃーにー": "Midjourney",

    "ランウェイ": "Runway",
    "らんうぇい": "Runway",

    "コヒア": "Cohere",
    "こひあ": "Cohere",

    "ヒューギングフェース": "Hugging Face",
    "ひゅーぎんぐふぇーす": "Hugging Face",

    # ビジネス系 / サービス名
    "ウーバー": "Uber",
    "うーばー": "Uber",

    "エアビーアンドビー": "Airbnb",
    "えあびーあんどびー": "Airbnb",

    "エクスペディア": "Expedia",
    "えくすぺでぃあ": "Expedia",

    "スポティファイ": "Spotify",
    "すぽてぃふぁい": "Spotify",

    "ネットフリックス": "Netflix",
    "ねっとふりっくす": "Netflix",

    "アマゾンプライム": "Amazon Prime",
    "あまぞんぷらいむ": "Amazon Prime",

    "ディズニープラス": "Disney+",
    "でぃずにーぷらす": "Disney+",

    "フールー": "Hulu",
    "ふーるー": "Hulu",

    "アベマ": "ABEMA",
    "あべま": "ABEMA",

    "ユーネクスト": "U-NEXT",
    "ゆーねくすと": "U-NEXT",

    "ブッキングドットコム": "Booking.com",
    "ぶっきんぐどっとこむ": "Booking.com",

    "ゾゾタウン": "ZOZOTOWN",
    "ぞぞたうん": "ZOZOTOWN",

    "ペイペイ": "PayPay",
    "ぺいぺい": "PayPay",

    "ペイパル": "PayPal",
    "ぺいぱる": "PayPal",

    "ウーバーイーツ": "Uber Eats",
    "うーばーいーつ": "Uber Eats",

    "ビズリーチ": "ビズリーチ",
    "びずりーち": "ビズリーチ",

    "ワークス": "Works",
    "わーくす": "Works",

    "ランサーズ": "Lancers",
    "らんさーず": "Lancers",

    "クラウドワークス": "CrowdWorks",
    "くらうどわーくす": "CrowdWorks",

    "ユーチューブ": "YouTube",
    "ゆーちゅーぶ": "YouTube",

    "ティックトック": "TikTok",
    "てぃっくとっく": "TikTok",

    "インスタグラム": "Instagram",
    "いんすたぐらむ": "Instagram",

    "ツイッター": "Twitter",
    "ついったー": "Twitter",

    "フェイスブック": "Facebook",
    "ふぇいすぶっく": "Facebook",

    "ツイッチ": "Twitch",
    "ついっち": "Twitch",

    "TVer": "TVer",
    "ティーバー": "TVer",
    "てぃーばー": "TVer",

    "楽天ペイ": "楽天ペイ",
    "らくてんぺい": "楽天ペイ",

    "アップルペイ": "Apple Pay",
    "あっぷるぺい": "Apple Pay",

    "グーグルペイ": "Google Pay",
    "ぐーぐるぺい": "Google Pay",

    "スイカ": "Suica",
    "すいか": "Suica",

    "パスモ": "PASMO",
    "ぱすも": "PASMO",

    "LINE Pay": "LINE Pay",
    "ラインペイ": "LINE Pay",
    "らいんぺい": "LINE Pay",

    "auPAY": "auPAY",
    "エーユーペイ": "auPAY",
    "えーゆーぺい": "auPAY",

    "d払い": "d払い",
    "でぃーばらい": "d払い",

    "ベンモ": "Venmo",
    "べんも": "Venmo",

    "ストライプ": "Stripe",
    "すとらいぷ": "Stripe",

    "ジャパンタクシー": "JapanTaxi",
    "じゃぱんたくしー": "JapanTaxi",

    "スカイスキャナー": "Skyscanner",
    "すかいすきゃなー": "Skyscanner",

    "トリップアドバイザー": "TripAdvisor",
    "とりっぷあどばいざー": "TripAdvisor",

    "ユーデミー": "Udemy",
    "ゆーでみー": "Udemy",

    "コーセラ": "Coursera",
    "こーせら": "Coursera",

    "デュオリンゴ": "Duolingo",
    "でゅおりんご": "Duolingo",

    "イーベイ": "eBay",
    "いーべい": "eBay",

    "リンクトイン": "LinkedIn",
    "りんくといん": "LinkedIn",

    "フィットビット": "Fitbit",
    "ふぃっとびっと": "Fitbit",

    "ストラバ": "Strava",
    "すとらば": "Strava",

    "マイフィットネスパル": "MyFitnessPal",
    "まいふぃっとねすぱる": "MyFitnessPal",

    "スマートニュース": "SmartNews",
    "すまーとにゅーす": "SmartNews",

    "ライン": "LINE",
    "らいん": "LINE",

    "家計簿アプリ": "家計簿アプリ",
    "かけいぼあぷり": "家計簿アプリ",

    "マネーフォワード": "MoneyForward",
    "まねーふぉわーど": "MoneyForward",

    "グーグルドライブ": "Google Drive",
    "ぐーぐるどらいぶ": "Google Drive",

    "ワンドライブ": "OneDrive",
    "わんどらいぶ": "OneDrive",

    "アイクラウド": "iCloud",
    "あいくらうど": "iCloud",

    "ボックス": "Box",
    "ぼっくす": "Box",

    "スチーム": "Steam",
    "すちーむ": "Steam",

    "プレイステーション": "PlayStation",
    "ぷれいすてーしょん": "PlayStation",

    "Xbox": "Xbox",
    "エックスボックス": "Xbox",
    "えっくすぼっくす": "Xbox",

    "ニンテンドー": "Nintendo",
    "にんてんどー": "Nintendo",

    "フォートナイト": "Fortnite",
    "ふぉーとないと": "Fortnite",

    "パズドラ": "パズドラ",
    "ぱずどら": "パズドラ",

    "モンスト": "モンスト",
    "もんすと": "モンスト",

    "アップルミュージック": "Apple Music",
    "あっぷるみゅーじっく": "Apple Music",

    "アマゾンミュージック": "Amazon Music",
    "あまぞんみゅーじっく": "Amazon Music",

    "ユーチューブミュージック": "YouTube Music",
    "ゆーちゅーぶみゅーじっく": "YouTube Music",

    "サウンドクラウド": "SoundCloud",
    "さうんどくらうど": "SoundCloud",

    "ラジコ": "radiko",
    "らじこ": "radiko",

    "インスタ": "Instagram",
    "いんすた": "Instagram",

    "フリッカー": "Flickr",
    "ふりっかー": "Flickr",

    "ピクサベイ": "Pixabay",
    "ぴくさべい": "Pixabay",

    "アンスプラッシュ": "Unsplash",
    "あんすぷらっしゅ": "Unsplash",

    "ホットペッパー": "ホットペッパー",
    "ほっとぺっぱー": "ホットペッパー",

    "ぐるなび": "ぐるなび",
    "グルナビ": "ぐるなび",

    "価格ドットコム": "価格.com",
    "かかくどっとこむ": "価格.com",

    "アットコスメ": "@cosme",
    "あっとこすめ": "@cosme",

    "クラシル": "KURASHIRU",
    "くらしる": "KURASHIRU",

    "デリッシュキッチン": "DELISH KITCHEN",
    "でりっしゅきっちん": "DELISH KITCHEN",

    "レディット": "Reddit",
    "れでぃっと": "Reddit",

    "ピンタレスト": "Pinterest",
    "ぴんたれすと": "Pinterest",

    "ミディアム": "Medium",
    "みでぃあむ": "Medium",

    "クオラ": "Quora",
    "くおら": "Quora",

    "テンダー": "Tinder",
    "てんだー": "Tinder",

    "バンブル": "Bumble",
    "ばんぶる": "Bumble",

    "ティンダー": "Tinder",
    "てぃんだー": "Tinder",

    # ビジネス系 / ファイル・拡張子関連
    "ピーディーエフ": "PDF",
    "ぴーでぃーえふ": "PDF",

    "エクセル": "Excel",
    "えくせる": "Excel",

    "パワーポイント": "PowerPoint",
    "ぱわーぽいんと": "PowerPoint",

    "ワード": "Word",
    "わーど": "Word",

    "ジップ": "ZIP",
    "じっぷ": "ZIP",

    "シーエスブイ": "CSV",
    "しーえすぶい": "CSV",

    "ジェーペグ": "JPEG",
    "じぇーぺぐ": "JPEG",

    "ジェーピーイージー": "JPG",
    "じぇーぴーいーじー": "JPG",

    "ピーエヌジー": "PNG",
    "ぴーえぬじー": "PNG",

    "ジフ": "GIF",
    "じふ": "GIF",

    "エムピーフォー": "MP4",
    "えむぴーふぉー": "MP4",

    "エムピースリー": "MP3",
    "えむぴーすりー": "MP3",

    "ダブリューエーブイ": "WAV",
    "だぶりゅーえーぶい": "WAV",

    "エーエーシー": "AAC",
    "えーえーしー": "AAC",

    "エイチティーエムエル": "HTML",
    "えいちてぃーえむえる": "HTML",

    "シーエスエス": "CSS",
    "しーえすえす": "CSS",

    "ジェーエス": "JS",
    "じぇーえす": "JS",

    "ジャバスクリプト": "JavaScript",
    "じゃばすくりぷと": "JavaScript",

    "パイソン": "Python",
    "ぱいそん": "Python",

    "ジェーソン": "JSON",
    "じぇーそん": "JSON",

    # ビジネス系 / OS・デバイス関連
    "ウィンドウズ": "Windows",
    "うぃんどうず": "Windows",

    "マック": "Mac",
    "まっく": "Mac",

    "マックオーエス": "macOS",
    "まっくおーえす": "macOS",

    "リナックス": "Linux",
    "りなっくす": "Linux",

    "ウブントゥ": "Ubuntu",
    "うぶんとぅ": "Ubuntu",

    "アイオーエス": "iOS",
    "あいおーえす": "iOS",

    "アンドロイド": "Android",
    "あんどろいど": "Android",

    "アイフォン": "iPhone",
    "あいふぉん": "iPhone",

    "アイパッド": "iPad",
    "あいぱっど": "iPad",

    "アイポッド": "iPod",
    "あいぽっど": "iPod",

    "アップルウォッチ": "Apple Watch",
    "あっぷるうぉっち": "Apple Watch",

    "マックブック": "MacBook",
    "まっくぶっく": "MacBook",

    "アイマック": "iMac",
    "あいまっく": "iMac",

    "サーフェス": "Surface",
    "さーふぇす": "Surface",

    "ピクセル": "Pixel",
    "ぴくせる": "Pixel",

    "ギャラクシー": "Galaxy",
    "ぎゃらくしー": "Galaxy",

    "エクスペリア": "Xperia",
    "えくすぺりあ": "Xperia",

    "アクオス": "AQUOS",
    "あくおす": "AQUOS",

    "キンドル": "Kindle",
    "きんどる": "Kindle",

    "ファイヤータブレット": "Fire Tablet",
    "ふぁいやーたぶれっと": "Fire Tablet",

    "クロームブック": "Chromebook",
    "くろーむぶっく": "Chromebook",

    "クロームオーエス": "Chrome OS",
    "くろーむおーえす": "Chrome OS",

    "ニンテンドースイッチ": "Nintendo Switch",
    "にんてんどーすいっち": "Nintendo Switch",

    "プレイステーション": "PlayStation",
    "ぷれいすてーしょん": "PlayStation",

    "プレステ": "PlayStation",
    "ぷれすて": "PlayStation",

    "エックスボックス": "Xbox",
    "えっくすぼっくす": "Xbox",

    "アップルティーブイ": "Apple TV",
    "あっぷるてぃーぶい": "Apple TV",

    "ファイヤーティーブイ": "Fire TV",
    "ふぁいやーてぃーぶい": "Fire TV",

    "クロームキャスト": "Chromecast",
    "くろーむきゃすと": "Chromecast",

    "アレクサ": "Alexa",
    "あれくさ": "Alexa",

    "グーグルホーム": "Google Home",
    "ぐーぐるほーむ": "Google Home",

    "ホームポッド": "HomePod",
    "ほーむぽっど": "HomePod",

    "ウェアラブル": "ウェアラブル",
    "うぇあらぶる": "ウェアラブル",

    "アンドロイド": "Android",
    "あんどろいど": "Android",

    "アイオーエス": "iOS",
    "あいおーえす": "iOS",

    "アイフォン": "iPhone",
    "あいふぉん": "iPhone",

    "アイパッド": "iPad",
    "あいぱっど": "iPad",

    "アイポッド": "iPod",
    "あいぽっど": "iPod",

    "アップルウォッチ": "Apple Watch",
    "あっぷるうぉっち": "Apple Watch",

    "マックブック": "MacBook",
    "まっくぶっく": "MacBook",

    "アイマック": "iMac",
    "あいまっく": "iMac",

    "マックミニ": "Mac Mini",
    "まっくみに": "Mac Mini",

    "マックプロ": "Mac Pro",
    "まっくぷろ": "Mac Pro",

    "サーフェス": "Surface",
    "さーふぇす": "Surface",

    "キンドル": "Kindle",
    "きんどる": "Kindle",

    "アレクサ": "Alexa",
    "あれくさ": "Alexa",

    "グーグルホーム": "Google Home",
    "ぐーぐるほーむ": "Google Home",

    "ギャラクシー": "Galaxy",
    "ぎゃらくしー": "Galaxy",

    "エクスペリア": "Xperia",
    "えくすぺりあ": "Xperia",

    "アクオス": "AQUOS",
    "あくおす": "AQUOS",

    "ニンテンドースイッチ": "Nintendo Switch",
    "にんてんどうすいっち": "Nintendo Switch",

    "プレイステーション": "PlayStation",
    "ぷれいすてーしょん": "PlayStation",

    "エックスボックス": "Xbox",
    "えっくすぼっくす": "Xbox",

    "ユーエスビー": "USB",
    "ゆーえすびー": "USB",

    "エッチディーエムアイ": "HDMI",
    "えっちでぃーえむあい": "HDMI",

    "ブルートゥース": "Bluetooth",
    "ぶるーとゅーす": "Bluetooth",

    "ワイファイ": "Wi-Fi",
    "わいふぁい": "Wi-Fi",

    "CPU": "CPU",
    "シーピーユー": "CPU",
    "しーぴーゆー": "CPU",

    "GPU": "GPU",
    "ジーピーユー": "GPU",
    "じーぴーゆー": "GPU",

    # 用語系 / マーケティング用語
    "エスイーオー": "SEO",
    "えすいーおー": "SEO",

    "エスイーエム": "SEM",
    "えすいーえむ": "SEM",

    "ケーピーアイ": "KPI",
    "けーぴーあい": "KPI",

    "アールオーアイ": "ROI",
    "あーるおーあい": "ROI",

    "シーティーアール": "CTR",
    "しーてぃーあーる": "CTR",

    "シーピーシー": "CPC",
    "しーぴーしー": "CPC",

    "シーピーエー": "CPA",
    "しーぴーえー": "CPA",

    "シーピーエム": "CPM",
    "しーぴーえむ": "CPM",

    "コンバージョン": "CV",
    "こんばーじょん": "CV",

    "シーブイアール": "CVR",
    "しーぶいあーる": "CVR",

    "コンバージョンレート": "CVR",
    "こんばーじょんれーと": "CVR",

    "エルティーブイ": "LTV",
    "えるてぃーぶい": "LTV",

    "ライフタイムバリュー": "LTV",
    "らいふたいむばりゅー": "LTV",

    "シーティーエー": "CTA",
    "しーてぃーえー": "CTA",

    "コールトゥアクション": "CTA",
    "こーるとぅあくしょん": "CTA",

    "エルピー": "LP",
    "えるぴー": "LP",

    "ユーエックス": "UX",
    "ゆーえっくす": "UX",

    "ユーアイ": "UI",
    "ゆーあい": "UI",

    "エスエヌエス": "SNS",
    "えすえぬえす": "SNS",

    # 用語系 / ビジネス略語
    "ビートゥビー": "B2B",
    "びーとぅびー": "B2B",

    "ビートゥシー": "B2C",
    "びーとぅしー": "B2C",

    "シートゥシー": "C2C",
    "しーとぅしー": "C2C",

    "サース": "SaaS",
    "さーす": "SaaS",

    "ソフトウェアアズアサービス": "SaaS",
    "そふとうぇああずあさーびす": "SaaS",

    "パース": "PaaS",
    "ぱーす": "PaaS",

    "アイアース": "IaaS",
    "あいあーす": "IaaS",

    "エーピーアイ": "API",
    "えーぴーあい": "API",

    "ユーアイ": "UI",
    "ゆーあい": "UI",

    "ユーエックス": "UX",
    "ゆーえっくす": "UX",

    "アールアンドディー": "R&D",
    "あーるあんどでぃー": "R&D",

    "シーエスアール": "CSR",
    "しーえすあーる": "CSR",

    "イーエスジー": "ESG",
    "いーえすじー": "ESG",

    "アイピーオー": "IPO",
    "あいぴーおー": "IPO",

    "エムアンドエー": "M&A",
    "えむあんどえー": "M&A",

    "ケーピーアイ": "KPI",
    "けーぴーあい": "KPI",

    "オーケーアール": "OKR",
    "おーけーあーる": "OKR",

    "ピーディーシーエー": "PDCA",
    "ぴーでぃーしーえー": "PDCA",

    "シーアールエム": "CRM",
    "しーあーるえむ": "CRM",

    "エスエフエー": "SFA",
    "えすえふえー": "SFA",

    "イーアールピー": "ERP",
    "いーあーるぴー": "ERP",

    "エーアイ": "AI",
    "えーあい": "AI",

    "ディーエックス": "DX",
    "でぃーえっくす": "DX",

    "アイティー": "IT",
    "あいてぃー": "IT",

    "アイシーティー": "ICT",
    "あいしーてぃー": "ICT",

    "アイオーティー": "IoT",
    "あいおーてぃー": "IoT",

    "エヌエフティー": "NFT",
    "えぬえふてぃー": "NFT",

    "ブイアール": "VR",
    "ぶいあーる": "VR",

    "エーアール": "AR",
    "えーあーる": "AR",

    "エムアール": "MR",
    "えむあーる": "MR",

    "シーイーオー": "CEO",
    "しーいーおー": "CEO",

    "シーティーオー": "CTO",
    "しーてぃーおー": "CTO",

    "シーエフオー": "CFO",
    "しーえふおー": "CFO",

    "シーエムオー": "CMO",
    "しーえむおー": "CMO",

    "シーアイオー": "CIO",
    "しーあいおー": "CIO",

    "シーオーオー": "COO",
    "しーおーおー": "COO",

    "シーピーオー": "CPO",
    "しーぴーおー": "CPO",

    "シーエスオー": "CSO",
    "しーえすおー": "CSO",

    "バイスプレジデント": "VP",
    "ばいすぷれじでんと": "VP",

    "エヌディーエー": "NDA",
    "えぬでぃーえー": "NDA",

    "エスエルエー": "SLA",
    "えすえるえー": "SLA",

    "リクエストフォープロポーザル": "RFP",
    "りくえすとふぉーぷろぽーざる": "RFP",

    "アールエフピー": "RFP",
    "あーるえふぴー": "RFP",

    "プルーフオブコンセプト": "PoC",
    "ぷるーふおぶこんせぷと": "PoC",

    "ポック": "PoC",
    "ぽっく": "PoC",

    "エムブイピー": "MVP",
    "えむぶいぴー": "MVP",

    "ビーピーアール": "BPR",
    "びーぴーあーる": "BPR",

    "ビーピーオー": "BPO",
    "びーぴーおー": "BPO",

    "ビーピーエム": "BPM",
    "びーぴーえむ": "BPM",

    "エムティーオー": "MTO",
    "えむてぃーおー": "MTO",

    "エムティーエス": "MTS",
    "えむてぃーえす": "MTS",

    "オーティーオー": "OTO",
    "おーてぃーおー": "OTO",

    "ジーティーエム": "GTM",
    "じーてぃーえむ": "GTM",

    # 用語系 / 業界用語
    "ディーエックス": "DX",
    "でぃーえっくす": "DX",

    "デジタルトランスフォーメーション": "DX",
    "でじたるとらんすふぉーめーしょん": "DX",

    "アイオーティー": "IoT",
    "あいおーてぃー": "IoT",

    "フィンテック": "FinTech",
    "ふぃんてっく": "FinTech",

    "エヌエフティー": "NFT",
    "えぬえふてぃー": "NFT",

    "ウェブスリー": "Web3",
    "うぇぶすりー": "Web3",

    "ウェブスリーポイントゼロ": "Web3.0",
    "うぇぶすりーぽいんとぜろ": "Web3.0",

    "ディーエーオー": "DAO",
    "でぃーえーおー": "DAO",

    "ディーファイ": "DeFi",
    "でぃーふぁい": "DeFi",

    "ゲームファイ": "GameFi",
    "げーむふぁい": "GameFi",

    "ソーシャルファイ": "SocialFi",
    "そーしゃるふぁい": "SocialFi",

    "オープンソース": "OSS",
    "おーぷんそーす": "OSS",

    "オーエスエス": "OSS",
    "おーえすえす": "OSS",

    "デブオプス": "DevOps",
    "でぶおぷす": "DevOps",

    # 用語系 / 会計・財務用語
    "イービットダー": "EBITDA",
    "いーびっとだー": "EBITDA",

    "イービット": "EBIT",
    "いーびっと": "EBIT",

    "アールオーアイ": "ROI",
    "あーるおーあい": "ROI",

    "アールオーエー": "ROA",
    "あーるおーえー": "ROA",

    "アールオーイー": "ROE",
    "あーるおーいー": "ROE",

    "アールアールアール": "RRR",
    "あーるあーるあーる": "RRR",

    "エーアールアール": "ARR",
    "えーあーるあーる": "ARR",

    "エムアールアール": "MRR",
    "えむあーるあーる": "MRR",

    "エルティーブイ": "LTV",
    "えるてぃーぶい": "LTV",

    "アイエフアールエス": "IFRS",
    "あいえふあーるえす": "IFRS",

    "ピーエル": "P&L",
    "ぴーえる": "P&L",

    "ピーアンドエル": "P&L",
    "ぴーあんどえる": "P&L",

    "オーシーエフ": "OCF",
    "おーしーえふ": "OCF",

    "フリーキャッシュフロー": "FCF",
    "ふりーきゃっしゅふろー": "FCF",

    "エフシーエフ": "FCF",
    "えふしーえふ": "FCF",

    "ネットプレゼントバリュー": "NPV",
    "ねっとぷれぜんとばりゅー": "NPV",

    "エヌピーブイ": "NPV",
    "えぬぴーぶい": "NPV",

    "アイアールアール": "IRR",
    "あいあーるあーる": "IRR",

    "ワック": "WACC",
    "わっく": "WACC",

    "ケーピーアイ": "KPI",
    "けーぴーあい": "KPI",

    "ピーイーアール": "PER",
    "ぴーいーあーる": "PER",

    "ピービーアール": "PBR",
    "ぴーびーあーる": "PBR",

    "イーピーエス": "EPS",
    "いーぴーえす": "EPS",

    "ビーピーエス": "BPS",
    "びーぴーえす": "BPS",

    "プライベートエクイティ": "PE",
    "ぷらいべーとえくいてぃ": "PE",

    "アイピーオー": "IPO",
    "あいぴーおー": "IPO",

    # 日常トレンド / エンタメ・メディア
    "ネットフリックス": "Netflix",
    "ねっとふりっくす": "Netflix",
    "ネトフリ": "Netflix",
    "ねとふり": "Netflix",

    "ユーチューブ": "YouTube",
    "ゆーちゅーぶ": "YouTube",

    "スポティファイ": "Spotify",
    "すぽてぃふぁい": "Spotify",

    "ティックトック": "TikTok",
    "てぃっくとっく": "TikTok",

    "インスタグラム": "Instagram",
    "いんすたぐらむ": "Instagram",
    "インスタ": "Instagram",
    "いんすた": "Instagram",

    "ツイッター": "Twitter",
    "ついったー": "Twitter",
    "エックス": "X",
    "えっくす": "X",

    "フェイスブック": "Facebook",
    "ふぇいすぶっく": "Facebook",

    "ツイッチ": "Twitch",
    "ついっち": "Twitch",

    "ディズニープラス": "Disney+",
    "でぃずにーぷらす": "Disney+",

    "アマゾンプライム": "Amazon Prime",
    "あまぞんぷらいむ": "Amazon Prime",
    "あまぷら": "Amazon Prime",
    "アマプラ": "Amazon Prime",

    "プライムビデオ": "Prime Video",
    "ぷらいむびでお": "Prime Video",

    "フールー": "Hulu",
    "ふーるー": "Hulu",

    "HBO": "HBO",
    "エイチビーオー": "HBO",
    "えいちびーおー": "HBO",

    "アップルティービー": "Apple TV+",
    "あっぷるてぃーびー": "Apple TV+",

    "パラマウントプラス": "Paramount+",
    "ぱらまうんとぷらす": "Paramount+",

    "ピーコック": "Peacock",
    "ぴーこっく": "Peacock",

    "アベマ": "ABEMA",
    "あべま": "ABEMA",

    "ユーネクスト": "U-NEXT",
    "ゆーねくすと": "U-NEXT",

    "ティーバー": "TVer",
    "てぃーばー": "TVer",

    "ソニー": "Sony",
    "そにー": "Sony",

    "プレイステーション": "PlayStation",
    "ぷれいすてーしょん": "PlayStation",

    "Xbox": "Xbox",
    "エックスボックス": "Xbox",
    "えっくすぼっくす": "Xbox",

    "Steam": "Steam",
    "スチーム": "Steam",
    "すちーむ": "Steam",

    "Epic Games": "Epic Games",
    "エピックゲームス": "Epic Games",
    "えぴっくげーむす": "Epic Games",

    "Unity": "Unity",
    "ユニティ": "Unity",
    "ゆにてぃ": "Unity",

    "Unreal Engine": "Unreal Engine",
    "アンリアルエンジン": "Unreal Engine",
    "あんりあるえんじん": "Unreal Engine",

    "フォートナイト": "Fortnite",
    "ふぉーとないと": "Fortnite",
    "ふぉとな": "Fortnite",
    "フォトナ": "Fortnite",

    "マインクラフト": "Minecraft",
    "まいんくらふと": "Minecraft",

    "マイクラ": "Minecraft",
    "まいくら": "Minecraft",

    "PUBG": "PUBG",
    "パブジー": "PUBG",
    "ぱぶじー": "PUBG",

    "エーペックス": "Apex Legends",
    "えーぺっくす": "Apex Legends",
    "えぺ": "Apex Legends",
    "エペ": "Apex Legends",

    "ヴァロラント": "VALORANT",
    "ゔぁろらんと": "VALORANT",

    "リーグオブレジェンド": "League of Legends",
    "りーぐおぶれじぇんど": "League of Legends",

    "LoL": "League of Legends",
    "エルオーエル": "League of Legends",
    "えるおーえる": "League of Legends",

    "オーバーウォッチ": "Overwatch",
    "おーばーうぉっち": "Overwatch",

    "パズドラ": "パズドラ",
    "ぱずどら": "パズドラ",

    "モンスト": "モンスト",
    "もんすと": "モンスト",

    "FGO": "FGO",
    "エフジーオー": "FGO",
    "えふじーおー": "FGO",

    "ウマ娘": "ウマ娘",
    "うまむすめ": "ウマ娘",

    "原神": "原神",
    "げんしん": "原神",

    "ブルーアーカイブ": "ブルーアーカイブ",
    "ぶるーあーかいぶ": "ブルーアーカイブ",

    "ブルアカ": "ブルーアーカイブ",
    "ぶるあか": "ブルーアーカイブ",

    "ポケモンGO": "ポケモンGO",
    "ぽけもんごー": "ポケモンGO",

    "ポケGO": "ポケモンGO",
    "ぽけごー": "ポケモンGO",

    "ディズニー": "Disney",
    "でぃずにー": "Disney",

    "ユニバーサルスタジオ": "Universal Studios",
    "ゆにばーさるすたじお": "Universal Studios",

    "USJ": "USJ",
    "ユーエスジェー": "USJ",
    "ゆーえすじぇー": "USJ",

    "ピクサー": "Pixar",
    "ぴくさー": "Pixar",

    "マーベル": "Marvel",
    "まーべる": "Marvel",

    "アップルミュージック": "Apple Music",
    "あっぷるみゅーじっく": "Apple Music",

    "アマゾンミュージック": "Amazon Music",
    "あまぞんみゅーじっく": "Amazon Music",

    "ユーチューブミュージック": "YouTube Music",
    "ゆーちゅーぶみゅーじっく": "YouTube Music",

    "サウンドクラウド": "SoundCloud",
    "さうんどくらうど": "SoundCloud",

    "ティックトックミュージック": "TikTok Music",
    "てぃっくとっくみゅーじっく": "TikTok Music",

    "オーディブル": "Audible",
    "おーでぃぶる": "Audible",

    "キンドル": "Kindle",
    "きんどる": "Kindle",

    "Kindle Unlimited": "Kindle Unlimited",
    "きんどるあんりみてっど": "Kindle Unlimited",

    "LINEマンガ": "LINEマンガ",
    "らいんまんが": "LINEマンガ",

    "集英社": "集英社",
    "しゅうえいしゃ": "集英社",

    "講談社": "講談社",
    "こうだんしゃ": "講談社",

    "小学館": "小学館",
    "しょうがくかん": "小学館",

    "角川": "KADOKAWA",
    "かどかわ": "KADOKAWA",

    "白泉社": "白泉社",
    "はくせんしゃ": "白泉社",

    "秋田書店": "秋田書店",
    "あきたしょてん": "秋田書店",

    # 日常トレンド系 / ショッピング・EC
    "ゾゾタウン": "ZOZOTOWN",
    "ぞぞたうん": "ZOZOTOWN",

    "キューテン": "Qoo10",
    "きゅーてん": "Qoo10",

    "アリエクスプレス": "AliExpress",
    "ありえくすぷれす": "AliExpress",

    "ショピファイ": "Shopify",
    "しょぴふぁい": "Shopify",

    "ベイス": "BASE",
    "べいす": "BASE",

    "ペイペイ": "PayPay",
    "ぺいぺい": "PayPay",

    "ラインペイ": "LINE Pay",
    "らいんぺい": "LINE Pay",

    "メルペイ": "メルペイ",
    "めるぺい": "メルペイ",

    "ファミペイ": "ファミペイ",
    "ふぁみぺい": "ファミペイ",

    "auペイ": "auPAY",
    "えーゆーぺい": "auPAY",

    "ディーばらい": "d払い",
    "でぃーばらい": "d払い",

    # 日常トレンド系 / ライフスタイル
    "サブスク": "サブスク",
    "さぶすく": "サブスク",

    "テレワーク": "テレワーク",
    "てれわーく": "テレワーク",

    "リモートワーク": "リモートワーク",
    "りもーとわーく": "リモートワーク",

    "ワーケーション": "ワーケーション",
    "わーけーしょん": "ワーケーション",

    "ノマドワーク": "ノマドワーク",
    "のまどわーく": "ノマドワーク",

    "腸活": "腸活",
    "ちょうかつ": "腸活",
    "超活": "腸活",
    "長活": "腸活",

    "推し活": "推し活",
    "おしかつ": "推し活",

    "朝活": "朝活",
    "あさかつ": "朝活",

    "夜活": "夜活",
    "よるかつ": "夜活",

    "婚活": "婚活",
    "こんかつ": "婚活",

    "就活": "就活",
    "しゅうかつ": "就活",

    "終活": "終活",
    "しゅうかつ": "終活",

    "断捨離": "断捨離",
    "だんしゃり": "断捨離",

    "ミニマリスト": "ミニマリスト",
    "みにまりすと": "ミニマリスト",

    "ゼロウェイスト": "ゼロウェイスト",
    "ぜろうぇいすと": "ゼロウェイスト",

    "SDGs": "SDGs",
    "エスディージーズ": "SDGs",
    "えすでぃーじーず": "SDGs",

    # 日常トレンド系 / 新語・流行語
    "バズる": "バズる",
    "ばずる": "バズる",

    "エモい": "エモい",
    "えもい": "エモい",

    "推し": "推し",
    "おし": "推し",

    "推し活": "推し活",
    "おしかつ": "推し活",

    "ガチャ": "ガチャ",
    "がちゃ": "ガチャ",

    "親ガチャ": "親ガチャ",
    "おやがちゃ": "親ガチャ",

    "課金": "課金",
    "かきん": "課金",

    "マウント": "マウント",
    "まうんと": "マウント",

    "フラグ": "フラグ",
    "ふらぐ": "フラグ",

    "ワンチャン": "ワンチャン",
    "わんちゃん": "ワンチャン",

    "詰んだ": "詰んだ",
    "つんだ": "詰んだ",

    "オワコン": "オワコン",
    "おわこん": "オワコン",

    "Z世代": "Z世代",
    "ぜっとせだい": "Z世代",

    "ゆとり世代": "ゆとり世代",
    "ゆとりせだい": "ゆとり世代",

    "ミレニアル世代": "ミレニアル世代",
    "みれにあるせだい": "ミレニアル世代",

    "チルする": "チルする",
    "ちるする": "チルする",

    "映える": "映える",
    "ばえる": "映える",

    "インスタ映え": "インスタ映え",
    "いんすたばえ": "インスタ映え",

    "タイパ": "タイパ",
    "たいぱ": "タイパ",

    "コスパ": "コスパ",
    "こすぱ": "コスパ",

    "ファスト映画": "ファスト映画",
    "ふぁすとえいが": "ファスト映画",

    "パリピ": "パリピ",
    "ぱりぴ": "パリピ",

    "陽キャ": "陽キャ",
    "ようきゃ": "陽キャ",

    "陰キャ": "陰キャ",
    "いんきゃ": "陰キャ",

    "ググる": "ググる",
    "ぐぐる": "ググる",

    "ポチる": "ポチる",
    "ぽちる": "ポチる",

    "サブスク": "サブスク",
    "さぶすく": "サブスク",

    "NFT": "NFT",
    "エヌエフティー": "NFT",
    "えぬえふてぃー": "NFT",

    "メタバース": "メタバース",
    "めたばーす": "メタバース",

    "Web3": "Web3",
    "ウェブスリー": "Web3",
    "うぇぶすりー": "Web3",

    "DeFi": "DeFi",
    "ディーファイ": "DeFi",
    "でぃーふぁい": "DeFi",

    "VTuber": "VTuber",
    "ブイチューバー": "VTuber",
    "ぶいちゅーばー": "VTuber",

    "配信者": "配信者",
    "はいしんしゃ": "配信者",

    "投げ銭": "投げ銭",
    "なげせん": "投げ銭",

    "スパチャ": "スパチャ",
    "すぱちゃ": "スパチャ",

    "チャンネル登録": "チャンネル登録",
    "ちゃんねるとうろく": "チャンネル登録",

    "チャンネル": "チャンネル",
    "ちゃんねる": "チャンネル",

    "ソロ活": "ソロ活",
    "そろかつ": "ソロ活",

}


