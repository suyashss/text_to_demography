1. Create a small evaluation set - DONE
2. Evaluation code - check if yaml files/strings are close - DONE
3. Convert evaluation set to HF format - DONE 
4. Upload evaluation set to huggingface - DONE
5. Do zero-shot evaluation of codellama on evaluation set - DONE
6. Create set of training examples from demes repo - DONE
    i. Find examples from demes documentation - DONE
    ii. Create a description for each yaml - DONE 
7. Create more synthetic training examples from manually created ones
    i. Ask GPT4 to convert manual example (yaml,description) pair to a 
    ii. Ask GPT4 to re-write each description 10 ways - so we get (yaml: [description1, description2,..., description 10])
    ii. Fill templates in with random values and choose one description
    iii. Accept examples where the yaml is recognized as valid by the demes program
8. Convert training set to pandas
9. Upload training set to huggingface