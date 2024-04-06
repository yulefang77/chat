def read_file(filename):
	with open(filename, 'r', encoding='utf-8-sig') as f:
		lines = []
		for line in f:
			lines.append(line.strip())			
	return lines


def convert(lines):
	s = []
	allen_msg_count = 0
	viki_msg_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_pic_count = 0
	viki_pic_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			for msg in s[2:]:
				if msg == '貼圖':
					allen_sticker_count += 1
				elif msg == '圖片':
					allen_pic_count += 1
				else:
					allen_msg_count += len(msg)
		elif name == 'Viki':
			for msg in s[2:]:
				if msg == '貼圖':
					viki_sticker_count += 1
				elif msg == '圖片':
					viki_pic_count += 1
				else:
					viki_msg_count += len(msg)

	print('Allen說了', allen_msg_count, '個字。')
	print('Allen傳了', allen_sticker_count, '個貼圖。')
	print('Allen傳了', allen_pic_count, '個圖片。')
	print('Viki說了', viki_msg_count, '個字。')
	print('Viki傳了', viki_sticker_count, '個貼圖。')
	print('Viki傳了', viki_pic_count, '個圖片。')

def write_file(filename, lines):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('Line-Viki.txt')
	lines = convert(lines)
	# write_file('output.txt', lines)

main()