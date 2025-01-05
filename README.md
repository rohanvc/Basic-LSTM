<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#Usage">Usage</a></li>
    <li><a href="#Contributing">Contributing</a></li>
    <li><a href="#Contact">Contact</a></li>
    <li><a href="#Additional Resources">Additional Resources</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Product Name Screen Shot][product-screenshot]

This project is a basic stock markey predictor. It is a good intro into how to use LSTMs. We create a simple LSTM that uses the closing price of the trailing 3 days to predict the closing price of the current day (Target Date). It currently runs on Microsoft's Stock Market Data, but can be easily configured to run on any CSV file. 

### Results: 

#### Training, Validation, and Test Data Splits
![Data Splits][data-splits]

#### Training Results
![Training Results][training-results]

#### Validation Results
![Validation Results][validation-results]

#### Overall Results
![Overall Results][Overall-results]

#### Recursive Results
![Recursive Results][Recursive-results]

For such a simple LSTM that only uses one variable, the results are not bad. However, do not use this to make real stock market trades, as this is partially overfitted for Microsoft's data. We can also see that the recursive predictions do not really work well with this LSTM, as they are generally bad at extrapolating data. 


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

For this project I used the following packages: 

  1. TensorFlow: Used to build the LSTM.
  2. Pandas: Used to read in Stock Data from CSV and data preperations.
  3. Numpy: Used to do matrix operations. 
  4. Matplotlib: Used to make the graphs.
  5. Kaggle: Used to download MSFT CSV Data. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Make sure you have the above packages installed. 
   ```sh
   pip install TensorFlow Pandas Numpy Matplotlib
   ```
2. Clone the repo
   ```sh
   git clone https://github.com/rohanvc/Basic-LSTM.git
   ```
3. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin github_username/repo_name
   git remote -v # confirm the changes
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Rohan Chaturvedula - [Linkedin](https://www.linkedin.com/in/rohan-chaturvedula/) - rchat10@gmail.com


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Additonal Resources

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Video Explanation of the Code by Greg Hogg](https://www.youtube.com/watch?v=CbTU92pbDKw)
* [Paper From Carnegie Mellon on LSTMs](https://deeplearning.cs.cmu.edu/S23/document/readings/LSTM.pdf)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/Stock.webp
[data-splits]: images/dataSplits.png
[training-results]: images/TrainingResults.png
[validation-results]: images/ValidationResults.png
[overall-results]: images/OverallResults.png
[recursive-results]: images/RecursiveResults.png

