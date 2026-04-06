import git_parser
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def generate_histogram(username: str) -> plt.Figure:
    results = git_parser.get_commit_from_name(username)
    df = pd.DataFrame(results)

    # 1. Ensure 'date' is a datetime object
    df['date'] = pd.to_datetime(df['date'])

    # 2. Extract Day of Week (0=Monday, 6=Sunday)
    df['day'] = df['date'].dt.day_name()
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # 3. Define Time Blocks
    # 0-6: Late Night, 6-12: Morning, 12-18: Afternoon, 18-24: Early Night
    bins = [0, 6, 12, 18, 24]
    labels = ['Late Night', 'Morning', 'Afternoon', 'Early Night']
    df['time_block'] = pd.cut(df['date'].dt.hour, bins=bins, labels=labels, right=False)

    # 4. Create Pivot Table for the Histogram
    # We use size to count occurrences in each bucket
    pivot_table = df.groupby(['day', 'time_block'], observed=False).size().unstack(fill_value=0)
    
    # Reorder to ensure logical flow
    pivot_table = pivot_table.reindex(index=day_order, columns=labels)

    # 5. Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(pivot_table, annot=True, fmt="d", cmap="YlGnBu", ax=ax)
    
    ax.set_title(f"Commit Activity for {username}")
    ax.set_xlabel("Time of Day")
    ax.set_ylabel("Day of Week")

    return fig