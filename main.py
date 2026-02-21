# 税込価格
apple_price = 200
rice_ball_price = 180
tea_price = 150

# 原価
apple_cost = 70
rice_ball_cost = 63
tea_cost = 65

input_item = input('購入したい商品を選んでください。A＝おにぎり、B＝お茶、C＝りんご：')
if input_item == A:
    price = rice_ball_price
    cost = rice_ball_cost
elif input_item == B:
    price = tea_price
    cost = tea_cost
elif input_item == C:
    price = apple_price
    cost = apple_cost
else:
    print('その商品は扱っていません')

benefit_per_item = price - cost

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
    total_price = price * 0.9 * count
    print('10%割引です')
else:
    total_price = price * 0.8 * count
    print('20%割引です')

print('購入する商品の個数は' + str(count) + '個です')

if total_price >= 500:
    input_coupon = input('クーポンを使いますか？yes/no：')
    if input_coupon == yes:
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

input_staff = input('あなたは店員ですか？yes/no:')
if input_staff == yes:
    print('店員用画面を表示します')
    print('売上=' + str(total_price) + '円')
    benefit = benefit_per_item * count
    print('利益=' + str(benefit) + '円')
elif input_staff == no:
    print('お買い上げありがとうございました！')
