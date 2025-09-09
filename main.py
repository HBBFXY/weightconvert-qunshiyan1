weight = input("请输入带有字符的重量")
if weight[-2:] in ['kg']:
  qianke = (eval (weight[0:-2]))/2.2046
  print("对应的公制重量为{:.3f}公斤".format(qianke))
elif weight[-2:] in ['pd']:
  bang = (eval (weight[0:-2]))*2.2046
  print("对应的英镑重量为{:.3f}磅".format(bang))
else:
  print("输入格式错误")
