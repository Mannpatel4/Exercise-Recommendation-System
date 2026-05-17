import pandas as pd

class ExerciseRecommendationSystem:

    def __init__(self,csv_file):

        # Load dataset
        self.original_df = pd.read_csv(csv_file)

        # Working dataframe
        self.df = self.original_df.copy()

    # RESET DATA
    def reset(self):
        self.df =self.original_df.copy()
        return self
    
    # 1. FILTER BY GOAL
    def filter_by_goal(self,goal):
        self.df = self.df[self.df["Goal"].astype(str).str.strip().str.lower() == goal]
        return self
    
    # 2. FILTER BY DIFFICULTY
    def filter_by_difficulty(self,difficulty):
        self.df = self.df[self.df['Difficulty'].astype(str).str.strip().str.lower() == difficulty]
        return self
    
    # 3. FILTER BY LOCATION
    def filter_by_location(self,location):
        self.df = self.df[self.df['Workout_Location'].astype(str).str.strip().str.lower() == location]
        return self
    
    # SHOW RECOMMENDATIONS
    def recommend(self,n=10):
        if len(self.df) == 0:
            return None
        result_df = self.df[["Exercise", "Main_Muscle", "Equipment"]].head(n)
        return result_df.to_dict('records')

# MAIN PROGRAM
if __name__ == "__main__":

    # Load CSV
    recommender = ExerciseRecommendationSystem('exercise.csv')

    # USER INPUT
    print("\nGOAL OPTIONS:")
    print("Muscle Gain")
    print("Fat Loss")
    print("Weight Gain")
    print("Weight Loss")

    goal = input("\nEnter Goal: ")

    print("\nDIFFICULTY OPTIONS:")
    print("Beginner")
    print("Intermediate")
    print("Advanced")

    difficulty = input("\nEnter Difficulty: ")

    print("\nLOCATION OPTIONS:")
    print("Gym")
    print("Home With Equipment")
    print("Home Without Equipment")

    location = input("\nEnter Location: ")

    # PIPELINE
    (recommender.reset().filter_by_goal(goal).filter_by_difficulty(difficulty).filter_by_location(location).recommend())