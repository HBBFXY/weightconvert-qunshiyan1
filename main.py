weight = input("请输入带有字符的重量")
if weight[-2:] in ['kg']:
  bang = (eval (weight[0:-2]))/2.2046
  print("对应的英制重量为{:.3f}磅".format(bang))
elif weight[-2:] in ['pd']:
  qinake = (eval (weight[0:-2]))*2.2046
  print("对应的公镑重量为{:.3f}公斤".format(qianke))
else:
  print("输入格式错误")
