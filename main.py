# 税込価格
apple_price = 200
rice_ball_price = 180
tea_price = 150

# 原価
apple_cost = 70
rice_ball_cost = 63
tea_cost = 65

# input() は 文字列（str型） を返す
input_item = input('購入したい商品を一つだけ選んでください。0:おにぎり、1:お茶、2:りんご：')
item = int(input_item)
if item == 0 or item == 1 or item == 2:
    if item == 0:
        price = rice_ball_price
        cost = rice_ball_cost
    elif item == 1:
        price = tea_price
        cost = tea_cost
    elif item == 2:
        price = apple_price
        cost = apple_cost

    # 文字列は''で囲う
    # 変数 = input('コンソールに表示したい文字列')
    input_money = input('所持金を入力してください：')
    money = int(input_money)

    # 整数除算 // 割り算して小数点以下を切り捨てる
    count_max = money // price
    print(str(count_max) + '個まで買えます')

    input_count = input('購入する商品の個数を入力してください：')
    count = int(input_count)
    # 割引システム。5個以上なら10%割引、10個以上なら20%割引
    # ifは行末にコロン
    if count <= 4:
        total_price = price * count
    elif 5 <= count <= 9:
        total_price = price * count * 9 // 10
        print('10%割引です')
    else:
        total_price = price * count * 8 // 10
        print('20%割引です')

    print('購入する商品の個数は' + str(count) + '個です')

    if total_price >= 500:
        input_coupon = input('クーポンを使いますか？yes0/no1：')
        coupon = int(input_coupon)
        if coupon == 0:
            total_price -= 100

    print('支払い金額は' + str(total_price) + '円です')

    # money と total_price の比較結果によって条件を分岐してください
    # 条件式の中のイコールは==（2個）
    if money > total_price:
        print('商品を' + str(count) + '個買いました')
        print('お釣りは' + str(money - total_price) +'円です')
    elif money == total_price:
        print('商品を' + str(count) + '個買いました')
        print('財布が空になりました')
    else:
        print('お金が' + str(total_price) + '円足りません')
        print('商品を買えませんでした')

    input_staff = input('あなたは店員ですか？yes0/no1:')
    staff = int(input_staff)
    if staff == 0:
        print('店員用画面を表示します')
        print('売上=' + str(total_price) + '円')
        benefit = total_price - cost * count
        print('利益=' + str(benefit) + '円')
    elif staff == 1:
        print('お買い上げありがとうございました！')
else:
        print('その商品は扱っていません')
