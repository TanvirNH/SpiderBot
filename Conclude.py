"""
Copyright 2022

Licensed under the GNU General Public License, Version 3.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

https://www.gnu.org/licenses/gpl-3.0.en.html

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# Import

from Container import Contain



# Functions

def Conclude(categories, file_names):
    """
    -------------------------------------------------------
    
    Use: Conclude(category, file_names)
    -------------------------------------------------------
    Parameters:
       x
    Returns:
       x
    ------------------------------------------------------
    """

    Collection = genCollection(categories, file_names)
    Collection_length = len(Collection)
    print(Collection)


   
    file_Collection = open("feature\\" + "Collection.txt", "w+", encoding="utf8")
    file_Collection_lenth = open("train\\" + "Collection_len.txt", "w+", encoding="utf8")

    file_Collection_lenth.write(str(Collection_length))

    for g in Collection:
       file_Collection.write(g + "\n")
    
    file_Collection.close()

    print("\n")
    for c in categories:

       category = c 
       counter = 1

       for i in file_names:
         word_list = Extract("dataset\\" + category + "\\" + i) 
         b_feature = genBinFeature(Collection, word_list)
         print(":: Category [{}] ~ File [{}] ::".format(category, i))
         print(b_feature, "\n\n")


    
         bin_file_name = "feature\\" + category + "\\" + category + "_bf" + str(counter) + ".txt"
         file_bf = open(bin_file_name, "w+", encoding="utf8")

         for k in range(len(Collection)):
            file_bf.write("{}\n".format(b_feature[k]))

         file_bf.close()
         counter += 1

    
    for c in categories:

      category = c 
      counter = 1

      for j in file_names:
         word_list = Extract("dataset\\" + category + "\\" + j) 
         wordlist_length = len(word_list)
         TEXT_FEATURE = genTFreqFeature(Collection, word_list)
         print(":: Category [{}] ~ File [{}] ::".format(category, j))
         print(TEXT_FEATURE, "\n\n")


         
         length_file_name = "feature\\" + category + "\\" + category + "_len" + str(counter) + ".txt"
         tf_file_name = "feature\\" + category + "\\" + category + "_tf" + str(counter) + ".txt"

         file_len_tf = open(length_file_name, "w+", encoding="utf8")
         file_len_tf.write(str(wordlist_length))

         file_tf = open(tf_file_name, "w+", encoding="utf8")

         for l in range(len(Collection)):
            file_tf.write("{}\n".format(TEXT_FEATURE[l]))

         file_tf.close()
         counter += 1


def genCollection(categories, file_names):
    """
    -------------------------------------------------------
    Generate Text Collection for the given categories

    Use: Collection = genCollection(categories)
    -------------------------------------------------------
    Parameters:
       x
    Returns:
       x
    ------------------------------------------------------
    """

    Collection = []

   # Iterating through categories
    for c in categories:

       category = c # Select current category

       # Extract Data from Current Category
       for j in file_names:
         word_list = Extract("dataset\\" + category + "\\" + j) 

      
         for k in word_list:
            
            
            if k not in Collection:
               Collection.append(k)

    return Collection



def genBinFeature(Collection, word_list):
    """
    -------------------------------------------------------
    Generate Binary Feature word list from passed in text
    Collection and word_list

    Use: b_feature = genBinFeature(Collection, word_list)
    -------------------------------------------------------
    Parameters:
       x
    Returns:
       x
    ------------------------------------------------------
    """

    b_feature = []

    for _ in range(len(Collection)):
      b_feature.append(0)
      
    for j in range(len(Collection)):
      if Collection[j] in word_list:
         b_feature[j] = 1

    return b_feature



def genTFreqFeature(Collection, word_list):
    """
    -------------------------------------------------------
    Generate Binary Feature word list from passed in text
    Collection and word_list

    Use: TEXT_FEATURE = genTFreqFeature(Collection, word_list)
    -------------------------------------------------------
    Parameters:
       x
    Returns:
       x
    ------------------------------------------------------
    """

    TEXT_FEATURE = []

    for _ in range(len(Collection)):
      TEXT_FEATURE.append(0)

    for i in range(len(Collection)):
      for j in range(len(word_list)):
         if Collection[i] == word_list[j]:
               TEXT_FEATURE[i] += 1

    return TEXT_FEATURE