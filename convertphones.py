# convertphones.py
# Takes list of words and finds appropriate phonemes
# If phoneme not found, an educated guess is made

from synthme import phonemes, util
import ast, re

def words_to_phonemes(words, use_pronunciation_dict=True):
	# Takes list of words and punctuation
	result = []
	for word in words:
		# Check if the word has been learned
		row = False
		if use_pronunciation_dict:
			row = util.get_pronunciation(word)
		if row:
			# Append the syllables in this word
			result.extend(row)
		else:
			# If not recognized, take an (un)educated guess
			blocked = phoneme_scan(word)
			result.extend(phoneme_blocks_to_list(blocked))
		result.append(phonemes.PAUSE_WORD)
	return result

def phoneme_blocks_to_list(blocks):
	blocks_list = re.findall("\[\d+\]", blocks)
	result = []
	for b in blocks_list:
		result.append(int(re.sub(r'\[(\d+)\]', r'\1', b)))
	return result


def phoneme_scan(word):
	while re.search("[a-zA-Z.,;!\?]", word): # Keep replacing letters with phonemes in brackets [] until there are no more letters
		word = replace_with_phoneme(word, r'ha', (phonemes.VOWEL_HA,))
		word = replace_with_phoneme(word, r'hu', (phonemes.VOWEL_HU,))
		word = replace_with_phoneme(word, r'he', (phonemes.VOWEL_HE,))
		word = replace_with_phoneme(word, r'a', (phonemes.VOWEL_A,))
                word = replace_with_phoneme(word, r'la', (phonemes.CONS_LA,))
		word = replace_with_phoneme(word, r'be', (phonemes.CONS_BE,))
		word = replace_with_phoneme(word, r'so', (phonemes.CONS_SO,))
		word = replace_with_phoneme(word, ".", (phonemes.PUNC_PERIOD,))
		word = replace_with_phoneme(word, ",", (phonemes.PUNC_COMMA,))
		word = replace_with_phoneme(word, ";", (phonemes.PUNC_COMMA,))
		word = replace_with_phoneme(word, "!", (phonemes.PUNC_EXCLAIM,))
	return word

def replace_with_phoneme(word, letters, phoneme_ids):
	result = ""
	for phoneme_id in phoneme_ids:
		result += "["+str(phoneme_id)+"]"
	return word.replace(letters, result)
