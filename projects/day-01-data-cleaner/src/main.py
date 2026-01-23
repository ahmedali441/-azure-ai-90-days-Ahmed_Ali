# Copy this ENTIRE code and save as src/main.py
import pandas as pd
import numpy as np
import os
from datetime import datetime

print("=" * 60)
print("DAY 1: SMART CSV DATA CLEANER - SIMPLE VERSION")
print("=" * 60)

def main():
    """Main function - runs everything"""
    
    # CREATE SAMPLE DATA RIGHT IN THE CODE (No file needed!)
    print("\n📊 CREATING SAMPLE DATA...")
    
    data = {
        'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Name': ['John Doe', 'Jane Smith', 'Robert Johnson', 'Alice Brown', 'John Doe', 
                 'Charlie Davis', '', 'Frank Gomez', 'Grace Hill', 'Henry Irving'],
        'Age': [30, None, 45, 28, 30, 33, 41, 29, 36, None],
        'Email': ['john@email.com', 'jane@email.com', 'bob@email.com', 
                  'alice@email.com', 'john@email.com', 'charlie@email.com',
                  'diana@email.com', 'frank@gmail', 'grace@email.com', 'henry@email.com'],
        'Salary': [75000, 82000, 92000, 68000, 75000, None, 88000, 72000, 95000, 89000],
    }
    
    df = pd.DataFrame(data)
    print(f"Created sample data with {len(df)} rows")
    
    # Show original data
    print("\n📋 ORIGINAL DATA:")
    print("-" * 40)
    print(df)
    
    # CLEAN THE DATA
    print("\n🧹 CLEANING DATA...")
    print("-" * 40)
    
    original_rows = len(df)
    
    # 1. Remove duplicates
    df = df.drop_duplicates()
    print(f"1. Removed {original_rows - len(df)} duplicate(s)")
    
    # 2. Fill missing ages with average
    avg_age = df['Age'].mean()
    df['Age'] = df['Age'].fillna(avg_age)
    print(f"2. Filled missing ages with average: {avg_age:.1f}")
    
    # 3. Fill missing salaries with median
    median_salary = df['Salary'].median()
    df['Salary'] = df['Salary'].fillna(median_salary)
    print(f"3. Filled missing salaries with median: {median_salary:.0f}")
    
    # 4. Fix empty names
    df['Name'] = df['Name'].fillna('Unknown')
    df['Name'] = df['Name'].apply(lambda x: 'Unknown' if str(x).strip() == '' else x)
    print("4. Fixed empty/blank names")
    
    # 5. Fix email format
    def fix_email(email):
        if '@' not in str(email):
            return f"{email}.com"
        return email
    
    df['Email'] = df['Email'].apply(fix_email)
    print("5. Fixed email formats")
    
    # Show cleaned data
    print("\n✅ CLEANED DATA:")
    print("-" * 40)
    print(df)
    
    # SAVE TO FILE
    print("\n💾 SAVING RESULTS...")
    
    # Create outputs folder if it doesn't exist
    os.makedirs('outputs', exist_ok=True)
    
    # Save cleaned data
    df.to_csv('outputs/cleaned_data.csv', index=False)
    print("✅ Saved cleaned data to: outputs/cleaned_data.csv")
    
    # Generate report
    report = f"""
    DATA CLEANING REPORT
    ====================
    Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    
    Summary:
    - Original rows: {original_rows}
    - Cleaned rows: {len(df)}
    - Duplicates removed: {original_rows - len(df)}
    
    Operations:
    1. Removed duplicate rows
    2. Filled missing ages with average ({avg_age:.1f})
    3. Filled missing salaries with median ({median_salary:.0f})
    4. Fixed empty names
    5. Fixed email formats
    
    ✅ Cleaning completed successfully!
    """
    
    with open('outputs/cleaning_report.txt', 'w') as f:
        f.write(report)
    
    print("✅ Generated report: outputs/cleaning_report.txt")
    
    print("\n" + "=" * 60)
    print("🎉 DAY 1 PROJECT COMPLETE!")
    print("=" * 60)
    print("\nNext: Run 'git add .' and 'git commit -m \"Day 1 complete\"'")

# Run the program
if __name__ == "__main__":
    main()
