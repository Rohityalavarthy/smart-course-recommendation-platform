# Personalized Academic Prediction System

A comprehensive machine learning system that provides personalized GPA predictions and course recommendations based on student academic history and collaborative filtering techniques.

## 🎯 Overview

This project showcases an end-to-end academic guidance platform that helps students make informed decisions about their course selection and academic planning. The system uses historical student data to predict academic performance and recommend courses tailored to individual student profiles.

## ✨ Features

- **GPA Prediction**: Predicts student GPA based on similar students' academic performance
- **Course Recommendations**: Multiple recommendation algorithms including:
  - Collaborative filtering based on student similarity
  - PageRank algorithm for course ranking
  - Branch-specific elective filtering
- **Web Interface**: User-friendly frontend for inputting academic data
- **Real-time Processing**: Backend API that processes requests and returns predictions
- **Multiple Recommendation Engines**: Four different recommendation approaches for comprehensive course suggestions

## 🏗️ Architecture

The system consists of three main components:

1. **Frontend**: Static web interface served from `/public` directory
2. **Backend**: Node.js Express server handling API requests and Python script execution
3. **ML Engine**: Python-based machine learning algorithms for predictions and recommendations

## 🛠️ Technologies Used

- **Backend**: Node.js, Express.js
- **ML/Data Processing**: Python, pandas, NumPy, NetworkX
- **Frontend**: HTML, JavaScript, CSS
- **Data Storage**: JSON, CSV files
- **Algorithms**: Jaccard Similarity, PageRank, Collaborative Filtering

## 📁 Project Structure

```
├── server.js                 # Express backend server
├── similarity_matrix.py      # Main ML processing script
├── final_modular.py         # Modular ML functions
├── package.json             # Node.js dependencies
├── public/                  # Static frontend files
│   ├── output.csv          # Course recommendations (Method 1)
│   ├── output_2.csv        # GPA predictions
│   ├── output_3.csv        # PageRank-based recommendations
│   └── output_4.csv        # Branch-specific recommendations
├── data.json               # User input data
├── CGPA.csv               # Historical student GPA data
├── CDCs.csv               # Course branch mappings
├── timetable.json         # Course scheduling data
└── Grade*.csv             # Student grade datasets
```

## 🚀 Quick Start

### Prerequisites

- Node.js (v14 or higher)
- Python (v3.7 or higher)
- Required Python packages: `pandas`, `numpy`, `networkx`

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd personalized-academic-prediction
   ```

2. **Install Node.js dependencies**
   ```bash
   npm install
   ```

3. **Install Python dependencies**
   ```bash
   pip install pandas numpy networkx
   ```

4. **Start the server**
   ```bash
   node server.js
   ```

5. **Access the application**
   Open your browser and navigate to: `http://localhost:2000`

## 📊 How It Works

### Data Flow

1. **User Input**: Student submits academic data through the web form
2. **Data Processing**: Server saves input to `data.json` and triggers Python ML scripts
3. **ML Analysis**: Python algorithms process the data using multiple approaches:
   - **Similarity-based filtering**: Finds students with similar course patterns
   - **GPA prediction**: Uses collaborative filtering to predict academic performance
   - **PageRank recommendations**: Ranks courses based on network analysis
   - **Branch filtering**: Filters recommendations based on degree requirements
4. **Results**: Generated recommendations and predictions saved as CSV files
5. **Display**: Frontend fetches and displays results to the user

### Recommendation Algorithms

#### 1. Collaborative Filtering (output.csv)
- Calculates Jaccard similarity between students based on courses taken
- Recommends courses from the top 25 most similar students
- Filters out core degree courses to focus on electives

#### 2. GPA Prediction (output_2.csv)
- Uses weighted similarity scores to predict student GPA
- Based on performance of similar students in the dataset

#### 3. PageRank Algorithm (output_3.csv)
- Creates a graph network of students and courses
- Uses PageRank to identify influential courses
- Recommends highly-ranked courses not yet taken by the student

#### 4. Branch-Specific Recommendations (output_4.csv)
- Filters recommendations based on student's preferred elective
- Finds students who took similar electives
- Recommends popular courses among that cohort

## 🔧 Configuration

### Data Files Required

- `CGPA.csv`: Historical student GPA records
- `CDCs.csv`: Course-to-branch mapping for filtering
- `Grade.csv`: Student course grades for training
- `Grade_Student.csv`: Extended student grade data
- `GradeDataWithBranch.csv`: Student data with branch information
- `timetable.json`: Course scheduling and metadata

### Supported Degree Branches

- B.E Chemical
- B.E Civil
- B.E Computer Science
- B.E Electrical & Electronic
- B.E Electronics & Communication
- B.E Electronics & Instrumentation
- B.E Mechanical
- B.Pharm
- M.Sc. Biological Sciences
- M.Sc. Chemistry
- M.Sc. Economics
- M.Sc. Mathematics
- M.Sc. Physics

## 📡 API Endpoints

### POST `/submit-form`
Accepts student academic data and triggers ML processing.

**Request Body:**
```json
{
  "beDegree": "B.E Computer Science",
  "mscDegree": "None",
  "preferredElective": "MACHINE LEARNING",
  "courses": [
    {
      "subject": "MATHEMATICS",
      "courseGrade": 9.0
    }
  ]
}
```

### GET `/get-csv-data/:csvId`
Retrieves processed recommendation results.

**Parameters:**
- `csv1`: Collaborative filtering recommendations
- `csv2`: GPA predictions
- `csv3`: PageRank-based recommendations
- `csv4`: Branch-specific recommendations

## 🔍 Example Usage

1. **Student Input**: Enter courses taken with grades, degree branch, and preferred elective
2. **Processing**: System analyzes input against historical data
3. **Results**: Receive four types of recommendations:
   - Top 5 courses based on student similarity
   - Predicted GPA for academic planning
   - Network-analysis based course suggestions
   - Branch-specific elective recommendations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## ⚠️ Important Notes

- This system is designed for educational and research purposes
- Ensure all required data files are present and properly formatted
- The system uses hardcoded file paths that may need adjustment for your environment
- Prediction accuracy depends on the quality and completeness of training data

## 🐛 Troubleshooting

- **Python script errors**: Ensure all required CSV files are present in the project directory
- **Port conflicts**: Change the PORT variable in server.js if port 2000 is occupied
- **Module not found**: Verify all Python dependencies are installed (`pip install pandas numpy networkx`)
- **File path errors**: Update hardcoded file paths in the Python scripts to match your directory structure

## 📧 Support

For issues and questions, please open an issue in the GitHub repository or refer to the project documentation.