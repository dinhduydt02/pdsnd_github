import time
import pandas as pd
import numpy as np

#Create dictionary of city data - 1st time for practicing
#Create dictionary of city data - 2nd time for practicing
#Create dictionary of city data - 3rd time for practicing
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_list = ['all','january','february','march','april','may','june','july','august','september','october','november','december']    
day_list = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input('Which city do you want to explore? ').lower()
            abc=CITY_DATA[city]
            break
        except:
            print('That\'s not a correct city!')

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Which month do you want to explore? ').lower()
    while month not in month_list:
        month = input('Pls input again! Which month do you want to explore? ')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Which day of week do you want to explore? ').lower()
    while day not in day_list:
        day = input('Not correct, pls input again! Which month do you want to explore? ')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    # convert Start time column to datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month, date_of_week
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday_name
    # filter by month
    if month != 'all':
        month = month_list.index(month)+1
        df = df[df['month']==month]
    if day != 'all':
        df = df[df['day_of_week']==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month: {}'.format(common_month))

    # TO DO: display the most common day of week
    common_date_of_week = df['day_of_week'].mode()[0]
    print('The most common day of week: {}'.format(common_date_of_week))

    # TO DO: display the most common start hour
    # extract month, date_of_week
    df['hour']=df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common start hour: {}'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station: {}'.format(common_start_station))
    
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station: {}'.format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    frequent_stations = df.groupby(['Start Station','End Station']).size().nlargest(1)
    print('The most frequent combination of start station and end station trip: {}'.format(frequent_stations))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_duration = df['Trip Duration'].sum()
    print('Total travel time: {} seconds'.format(trip_duration))
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time: {} seconds'.format(mean_travel_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_type = df.groupby(['User Type'])['User Type'].count()
    print('Counts of user types: {}'.format(count_user_type))
    
    # TO DO: Display counts of gender
    if 'Gender' in df:
        count_gender = df.groupby(['Gender'])['User Type'].count()
        print('Counts of gender: {}'.format(count_gender))
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_yob = df['Birth Year'].min()
        print('The earliest year of birth: {}'.format('%02d' % earliest_yob))

        most_recent_yob = df['Birth Year'].max()
        print('The most recent year of birth: {}'.format('%02d' % most_recent_yob))

        common_yob = df['Birth Year'].mode()[0]
        print('The most common year of birth: {}'.format('%02d' % common_yob))
    else:
        print('Birth year stats cannot be calculated because Gender does not appear in the dataframe')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    i=0
    while True:
        answer = input('\nWould you like to see more raw data? Enter yes or no.\n')
        if answer.lower() != 'yes':
            break
        print(df.iloc[i:(i+5)])
        i+=5

def main():
    while True:
        try:
            city, month, day = get_filters()
            df = load_data(city, month, day)

            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            display_raw_data(df)

            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break
        except:
            print('Data is invalid!')


if __name__ == "__main__":
	main()
