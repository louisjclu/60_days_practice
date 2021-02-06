import numpy as np
english_score = np.array([55,89,76,65,48,70])

math_score = np.array([60,85,60,68,np.nan,60])

chinese_score = np.array([65,90,82,72,66,77])

print('英文：\n最大值：'+str(np.max(english_score))+'\n最小值：'+str(np.min(english_score))+'\n成績平均：'+str(np.average(english_score))+'\n標準差：'+str(np.std(english_score))+'。')
print('------------------------------------')
print('數學：\n最大值：'+str(np.nanmax(math_score))+'\n最小值：'+str(np.nanmin(math_score))+'\n成績平均：'+str(np.nanmean(math_score))+'\n標準差：'+str(np.nanstd(math_score))+'。')
print('------------------------------------')
print('國文：\n最大值：'+str(np.max(chinese_score))+'\n最小值：'+str(np.min(chinese_score))+'\n成績平均：'+str(np.average(chinese_score))+'\n標準差：'+str(np.std(english_score))+'。')
print('------------------------------------')
print('------------------------------------')
print('------------------------------------')

math_score[4]=55

print('------------------------------------')
print('數學：\n最大值：'+str(np.nanmax(math_score))+'\n最小值：'+str(np.nanmin(math_score))+'\n成績平均：'+str(np.nanmean(math_score))+'\n標準差：'+str(np.nanstd(math_score))+'。')
print('------------------------------------')
print('英文與國文相關係數：')
print(np.corrcoef(english_score, chinese_score))
print('數學與國文相關係數')
print(np.corrcoef(math_score,chinese_score))