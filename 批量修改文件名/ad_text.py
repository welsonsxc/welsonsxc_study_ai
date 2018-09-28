import os
	if not os.path.isdir(dir2):
		return
	# 获取该目录下所有的文件名
	names=os.listdir(dir2)
	# 如果是文件 则重命名 如果是目录 则下钻并重命名
	for name in names:
		# path == dir2
		old_name = os.path.join(dir2, name)
		# 是目录啦~下钻~
		if os.path.isdir(old_name):
			remove_ad_text(old_name, ad_text)
		# 去掉垃圾广告词
		name = name.replace(ad_text,"")
		new_name = os.path.join(dir2,name)
		# 对文件重命名
		os.rename(old_name, new_name)

		
if __name__ == "__main__":
	remove_ad_text(r'C:\Users\welso\Desktop\test','[123]')