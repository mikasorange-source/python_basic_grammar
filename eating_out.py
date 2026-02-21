# 厳しめトーン
# 今月の食費予算（円）
input_monthly_budget = input('今月の食費予算は何円ですか？：')
monthly_budget = int(input_monthly_budget)

# 今月ここまでの食費実績（円）
# 家計簿を確認して入力する
input_spent_so_far = input('今月すでにいくら食費に使いましたか？：')
spent_so_far = int(input_spent_so_far)

# 今月残り日数（日）
# 閏年は考慮していない
input_month = input('今は何月ですか？：')
month = int(input_month)
input_date = input('今日は何日ですか？：')
date = int(input_date)
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month ==10 or month ==12:
  days_in_month = 31
elif month == 2:
  days_in_month = 28
elif month == 4 or month == 6 or month == 9 or month == 11:
  days_in_month = 30
days_left = days_in_month - date + 1
print('残り日数：' + str(days_left) + '日')

# 今日の外食予定額（円）
input_eatout_plan = input('今日の外食予定額は何円ですか？')
eatout_plan = int(input_eatout_plan)
print('今日の外食予定：' + str(eatout_plan) + '円')

remaining_budget = monthly_budget - spent_so_far
print('残り予算：' + str(remaining_budget) + '円')

# 0で割ってエラーにならないように
# NGの時は理由も伝える
if days_left <= 0:
  print('入力ミスです')
else:
    daily_limit = remaining_budget // days_left
    print('1日平均の食費上限：' + str(daily_limit) + '円')

    # 外食比率は60%固定とする
    # 60%は * 6 // 10 で小数を出さない
    eatout_limit = daily_limit * 6 // 10
    print('外食上限（60%）：' + str(eatout_limit) + '円')

    #OKでも甘くしない
    if remaining_budget < 0:
        print('赤字です')
        print('判定：NG')
    else:
        if eatout_limit < 300:
         print('判定：NG')
         print('外食上限が300円未満のため')
        elif eatout_plan <= eatout_limit:
         print('判定：OK')
         print('許容範囲内ですが、上限は' + str(eatout_limit) + '円です')
        elif eatout_plan > eatout_limit:
         over = eatout_plan - eatout_limit
         print('判定：NG')
         print(str(over) + '円オーバーです')
