# SpiderBot

## Introduction

- What is a Web Crawler?

The Web Crawler project searches the internet for data and stores it on specific web pages. A crawler is especially useful for finding up-to-date material since it is designed with multi-thread concepts in mind. In order to make a crawler bot, there is the utilization of Python's request module or Scrapy, an open-source Python crawler framework designed primarily for web scraping and data extraction through APIs. In this particular project, the web crawler will classify HTML pages by searching all the document's words for the number of keywords like the three categories' titles. In order to discover a category match, the most frequent word will be chosen.

## Introduction

The following are the topics which were put into focus:

- COVID-19

- Blue

- Human

## Implementation Guidelines

- Comments on code that is not self-explanatory should be kept to a bare minimum.
- Appropriate names for variables. There should be no need for naming standards to be
explained; they should be self-evident.
- Do not deviate from traditional Python naming conventions for variables, functions,
classes, and so on.
- There should be no hard-coded conditions; everything should be modular.
- Check to see whether your code is inefficient. However, although it is not required, a
complete program should work well.

## Implementation Guidelines

For the following reasons, this application will be developed in Python:

- Many built-in functions help to minimize the number of lines of code. As a consequence, a more straightforward code is required.
- Applicative, Imperative, and Object-Oriented programming techniques are among the options.
- The syntax is basic and straightforward, and it resembles pseudocode. It also works on a variety of platforms.
- There are many libraries available to extract data from CSV, HTML, and files and deal with networks.

## Implementation

The implementation program's primary goal is to determine the URL category of URL page HTML content. It was created using Natural Language Processing and Machine Learning. 

The implementation part is divided into the following sections:
- Data is trained using ml techniques.
- To generate datasets, NLP methods are used.
- A list of URLs makes up the URLs data set.
- Findings and conclusions
- Preprocessing of data.

The research aims to solve the URL categorization issue by using a supervised classification algorithm and a database with many categorized websites. A supervised classification should be learned to predict which category a web page belongs to.

## Programs Used

- Beautiful Soup: Beautiful Soup is a Python module that allows you to parse HTML and XML
files. It builds a parse tree for parsed pages, which may be used to extract data from HTML and is helpful for web scraping. In our application, we utilized Python's excellent soup web crawling module to crawl through the user-entered category. To extract the text from the HTML, we used to find all a built-in method in beautiful soup.

- Selenium: Selenium is a portable framework for web application testing.
Without having to learn a test scripting language, Selenium offers a playback tool for writing functional tests. Beautiful soup has certain restrictions, such as the inability to interact with the browser (i.e., clicking on buttons or links). Selenium overcomes this constraint and enables us to communicate with the browser. It's a tool for automating web browsers.

- XPath: The XPath query language is used to pick nodes from an XML document. Additionally, XPath may be used to calculate values from an XML document's content. The World Wide Web Consortium created XPath. When the web driver opens the browser to click on the search engine's URLs, we've imported XPath.

- Web driver: WebDriver is software that allows you to test web applications in various browsers and computer languages. Because WebDriver enables you to construct your tests in any programming language, you can now create more robust tests. We're utilizing chrome's web driver's API in our program, importing it, and executing our program with the assistance of selenium's built-in functionality.

## Setup for Experiments

The Python Experiment was put up in the following way:

- Data Gathering: 

A web crawler was created to retrieve HTML pages from DuckDuckGo's search engine using customized search queries and our defined categories. To aid supervised learning, the crawler organizes the first page of results into a folder structure. BeautifulSoup4 was used to create the queries, while urllib3 was used to retrieve and convert the HTML files to text files. The final result is an HTML file directory for search queries in one of our categories: Blue, Human, And Covid-19.

The outcome of executing the Web Crawler Function for the ‘Blue’ category is shown in the screenshot below:

![Screen Shot 2022-02-14 at 10 41 22 PM](https://user-images.githubusercontent.com/68251349/153988408-449ada0c-1d67-4d8f-8d18-694337a37a72.png)

## Preparation of Data (Feature Engineering)

The feature container parses each of our scraped HTML files and generates a text document containing all of the terms found on the page. For the convenience of usage, these text files are set up with one word per line. It works by searching an HTML file for terms and adding them to a text file. Each category has one of these text files. Blue, for example, would have a single text corpus including every word discovered in the meaning of blue HTML files.

The following function will check this list of keywords to determine whether any of the words in the corpus are present in the HTML file being scanned. This generates a binary list in which each index corresponds to a text corpus index. If a phrase from the current HTML file matches one of the terms in our collection of words linked to the current category, in this case, Blue, we would add a 1 to the relevant index.

Take, for example, A, which is a list of keywords found in each of the scanned AI words:
A = [“Ocean,” “Water,” “Colour,” “light,” “indigo,” “sky”]
Now let’s assume that we have this collection:
B = ["Sky," "Red," "Blood," "Hay," "Trees," "Tiel," "Pineapple," "Green"]
For this project, the Binary Feature Set for the HTML page that generated B, let us call it S, would be as follows:
S = [1, 0, 0, 1, 0, 0]
The indices of S match the indices of our text corpus – A, as indicated.
Before storing the presently scanned web file for subsequent use, the Binary Feature Extractor in this project compares it to the text corpus.

Then we count the number of times a word match occurs between the text corpus and the presently scanned HTML file using our TF-IDF Extractor. This works similarly to our Binary Feature Extractor. This instance, though, counts the number of terms in each category to give our classifier an idea of which words occur the most often.

The number of occurrences next to each word has now been produced, as shown:

![Screen Shot 2022-02-14 at 10 43 02 PM](https://user-images.githubusercontent.com/68251349/153988572-40fe98a4-b761-41f2-8007-064662ff9a77.png)

This data preparation is critical to the accuracy of our Learning and Training algorithms. The directories of HTML files are now converted into directories of text files.

## Construction of a Data Model (Learning and Training)

To make it easier to classify websites, all data collected in lists are saved as text documents. Dynamic programming is used to make this technique more efficient. Averaging the phrase frequencies of each category's terms produces the training data. Identifying the usual document lengths is also important.

A benefit of creating this training data was that the user could immediately put an unknown HTML page in the categorized folder after it was generated. The probability factor for each category will be computed once the text has been retrieved. The Naive Bayes Method employs the following formula. The value we will use to identify each category is P(Category | Document). The untitled document's most probable category is the one with the highest value. The following is the Probability Factor for a Document in a Specific Category:

![Screen Shot 2022-02-14 at 10 43 49 PM](https://user-images.githubusercontent.com/68251349/153988660-16d25aa8-4848-4b0a-b993-20fdcd1cb382.png)

![Screen Shot 2022-02-14 at 10 44 08 PM](https://user-images.githubusercontent.com/68251349/153988704-695198dc-c362-4ebf-b995-a62bb711c135.png)

In general, this section converts and analyzes numerical data from HTML pages to build a model that can classify a document into one of the available categories. Another advantage of this method is that it is not limited to a single category. This program will do the same task regardless of the number of categories or the size of the dataset. The output of the program is inspected and tested in the next section.

## Analysis of Experiments

The results of the Experiment are examined and tested in this section:

- Analysis

This Classifier uses Natural Language Processing and is based on the Naive Bayes Classification Algorithm. The following criteria were used to make the final classification for this Experiment:

![Screen Shot 2022-02-14 at 10 45 02 PM](https://user-images.githubusercontent.com/68251349/153988814-77351d7a-ae84-4afe-a78e-0fe78d92f5de.png)

![Screen Shot 2022-02-14 at 10 45 39 PM](https://user-images.githubusercontent.com/68251349/153988889-16c0e146-250c-42a8-9b6e-96bf31699bf9.png)

This is because adding just one step will slow down the process while not affect the final result. The degree to which this software correctly detects pages can be used to assess their quality. Based on the training dataset, a machine learning model can predict the HTML document category. In the same phase of data extraction. Before the stop words were removed, the average length of these papers was 2940 words; however, after removing the Stop Words, the length of these documents was decreased to 2269 words. This means that simply removing phrases like "I," "me," "myself," and others reduced the word list's length by 23%. Therefore, the chances of getting an accurate result were improved.

## Testing

Software testing is important in software development because it assesses software quality after a
programmer has created it. This process involves evaluating the information.

To evaluate the Classifier's test accuracy. To achieve this, we will need the following items:

- True Positive (TP): The Classifier predicted the category correctly.
- False Positive (FP): The Classifier fails to predict the category correctly.

## Results

The results of the Classifier program's tests are shown in the table below:

![Screen Shot 2022-02-14 at 10 46 47 PM](https://user-images.githubusercontent.com/68251349/153988999-080a2839-ca35-434d-b048-cb29cb231d1c.png)

The table is represented. The 1s indicate a positive result, while the 0s indicate a negative one. Only when two very similar topics, such as Covid19 and Human, are assessed can the Classifier give erroneous results, as seen in the table and graph. Some common words in both categories may have been included in the HTML pages used in the dataset or as the Unknown. It is possible that by expanding the dataset and creating bigger and more robust training features, this problem may be solved even more effectively. The following is a comparison of the Natural Language Processing Classifier Model and the Naive Bayes Classification Method:

- The Accuracy Score is calculated in the first step:

![Screen Shot 2022-02-14 at 10 47 09 PM](https://user-images.githubusercontent.com/68251349/153989037-25d99352-0821-4985-8b49-dc8373b03fe3.png)

- Calculating the Precision Score in Step 2:

![Screen Shot 2022-02-14 at 10 47 25 PM](https://user-images.githubusercontent.com/68251349/153989054-5d6d2184-2b3a-4b30-8850-e898d5d16fa2.png)

- In step three, we will calculate your recall score:

![Screen Shot 2022-02-14 at 10 47 47 PM](https://user-images.githubusercontent.com/68251349/153989100-d1f9e643-f871-4a04-ac44-725ee86494ad.png)

- In step four, we will calculate your F1 score.

![Screen Shot 2022-02-14 at 10 48 04 PM](https://user-images.githubusercontent.com/68251349/153989138-1f64e354-386e-42b8-a085-ef6c56e069ef.png)

With an F1 score of 0.8235, the Classifier Program has a low number of False Positives and False Negatives. This shows how successful the program is.
- Among the others, P (covid-19 | unknown) has the highest probability factor. As a result, it is the most probable scenario.
- Among the others, P (Blue | unknown) has the highest probability factor. As a result, it is the most probable scenario.
- Among the others, P (Blue | unknown) has the highest probability factor. As a result, it is the most probable scenario.
- Among the others, P (human | unknown) has the highest probability factor. As a result, it is the most probable scenario.

## Conclusion

Finally, because the entire program was constructed entirely with Artificial Intelligence techniques, we may assume that the following experiment produced an accurate result. There were no scripts or external libraries used. The Crawler, Extractor, Preparator, Trainer, and Classifier are among the smaller components of the Classifier software, each of which performs a specific task.

