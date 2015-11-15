from difflib import SequenceMatcher

def belongInSameGroup(article1, article2):
	titleMatch = SequenceMatcher(None,article1["title"],article2["title"])
	contentMatch = SequenceMatcher(None,article1["content"],article2["content"])
	matchIndex = titleMatch.ratio() * contentMatch.ratio() * 1000
	if matchIndex > 5:
		return True
	else:
		return False