from summary_tool import SummaryTool
from sttools import SiteParser

# Main method, just run "python summary_tool.py"
def main():

  # Demo
  # Content from: "http://thenextweb.com/apps/2013/03/21/swayy-discover-curate-content/"
  
	pageURL = 'http://nasional.tempo.co/read/news/2015/08/09/058690416/buntut-ribut-di-lp-malang-9-napi-terorisme-sudah-dipindah'
	siteparser = SiteParser(pageURL)
	siteparser.getContentBySite()

	title = siteparser.title
	content = siteparser.content

	# Create a SummaryTool object
	st = SummaryTool()

	# Build the sentences dictionary
	sentences_dic = st.get_sentences_ranks(content)

	# Build the summary with the sentences dictionary
	summary = st.get_summary(title, content, sentences_dic)

	# Print the summary
	print summary

  # Print the ratio between the summary length and the original length
	print ""
	print "Original Length %s" % (len(title) + len(content))
	print "Summary Length %s" % len(summary)
	print "Summary Ratio: %s" % round((100 - (100 * (float(len(summary)) / float((len(title) + len(content)))))), 2)

if __name__ == '__main__':
	main()