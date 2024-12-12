# app.py
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np

# Configuration and secrets management
def load_config():
    # In production, use st.secrets
    # For local development, you can use a config file
    pass

class SocialMediaAnalytics:
    def __init__(self):
        st.set_page_config(
            page_title="Social Media Analytics Dashboard",
            page_icon="📊",
            layout="wide"
        )
        
    def run(self):
        st.title("📱 Social Media Analytics Dashboard")
        
        # Sidebar for navigation
        self.create_sidebar()
        
        # Main content
        if st.session_state.get('page') == 'Overview':
            self.show_overview()
        elif st.session_state.get('page') == 'Engagement Analysis':
            self.show_engagement_analysis()
        elif st.session_state.get('page') == 'Content Analysis':
            self.show_content_analysis()
        elif st.session_state.get('page') == 'Audience Insights':
            self.show_audience_insights()
    
    def create_sidebar(self):
        with st.sidebar:
            st.header("Navigation")
            pages = ['Overview', 'Engagement Analysis', 
                    'Content Analysis', 'Audience Insights']
            
            if 'page' not in st.session_state:
                st.session_state.page = 'Overview'
                
            for page in pages:
                if st.button(page):
                    st.session_state.page = page
            
            st.sidebar.markdown("---")
            self.date_filter()
    
    def date_filter(self):
        st.sidebar.header("Date Range")
        
        # Default to last 30 days
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)
        
        start_date = st.sidebar.date_input("Start Date", start_date)
        end_date = st.sidebar.date_input("End Date", end_date)
        
        return start_date, end_date

    def show_overview(self):
        st.header("📈 Overview Dashboard")
        
        # Example metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            self.metric_card("Total Followers", "12,345", "+5.2%")
        with col2:
            self.metric_card("Engagement Rate", "3.8%", "-0.5%")
        with col3:
            self.metric_card("Total Posts", "283", "+12")
        with col4:
            self.metric_card("Avg. Likes", "456", "+2.1%")
            
        # Engagement over time chart
        self.plot_engagement_over_time()
        
        # Top performing content
        self.show_top_content()

    def metric_card(self, title, value, delta):
        st.metric(
            label=title,
            value=value,
            delta=delta
        )

    def plot_engagement_over_time(self):
        st.subheader("Engagement Over Time")
        
        # Example data
        dates = pd.date_range(start='2024-01-01', end='2024-01-31', freq='D')
        engagement = np.random.normal(100, 15, len(dates))
        
        df = pd.DataFrame({
            'Date': dates,
            'Engagement': engagement
        })
        
        fig = px.line(df, x='Date', y='Engagement',
                     title='Daily Engagement Trend')
        st.plotly_chart(fig, use_container_width=True)

    def show_top_content(self):
        st.subheader("Top Performing Content")
        
        # Example data
        data = {
            'Post': ['Image 1', 'Video 1', 'Image 2', 'Story 1', 'Video 2'],
            'Type': ['Image', 'Video', 'Image', 'Story', 'Video'],
            'Engagement': [1200, 980, 850, 750, 600],
            'Likes': [1000, 800, 700, 600, 500],
            'Comments': [200, 180, 150, 150, 100]
        }
        
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)

    def show_engagement_analysis(self):
        st.header("🎯 Engagement Analysis")
        
        # Engagement by content type
        self.plot_engagement_by_type()
        
        # Engagement distribution
        self.plot_engagement_distribution()

    def plot_engagement_by_type(self):
        st.subheader("Engagement by Content Type")
        
        # Example data
        data = {
            'Type': ['Images', 'Videos', 'Stories', 'Carousels'],
            'Engagement Rate': [4.2, 3.8, 3.1, 4.5]
        }
        
        df = pd.DataFrame(data)
        fig = px.bar(df, x='Type', y='Engagement Rate',
                    title='Average Engagement Rate by Content Type')
        st.plotly_chart(fig, use_container_width=True)

    def plot_engagement_distribution(self):
        st.subheader("Engagement Distribution")
        
        # Example data
        engagement = np.random.normal(100, 25, 1000)
        
        fig = px.histogram(engagement, title='Distribution of Engagement')
        st.plotly_chart(fig, use_container_width=True)

    def show_content_analysis(self):
        st.header("📝 Content Analysis")
        
        # Content calendar
        self.show_content_calendar()
        
        # Hashtag analysis
        self.show_hashtag_analysis()

    def show_content_calendar(self):
        st.subheader("Content Calendar")
        
        # Example calendar data
        calendar_data = pd.DataFrame({
            'Date': pd.date_range(start='2024-01-01', end='2024-01-07'),
            'Content Type': ['Image', 'Video', 'Story', 'Image', 'Video', 'Story', 'Image'],
            'Status': ['Posted', 'Posted', 'Posted', 'Scheduled', 'Scheduled', 'Draft', 'Draft']
        })
        
        st.dataframe(calendar_data, use_container_width=True)

    def show_hashtag_analysis(self):
        st.subheader("Hashtag Performance")
        
        # Example hashtag data
        hashtag_data = {
            'Hashtag': ['#tech', '#innovation', '#AI', '#future', '#coding'],
            'Usage Count': [45, 38, 32, 28, 25],
            'Avg Engagement': [420, 380, 350, 310, 290]
        }
        
        df = pd.DataFrame(hashtag_data)
        st.dataframe(df, use_container_width=True)

    def show_audience_insights(self):
        st.header("👥 Audience Insights")
        
        # Audience demographics
        self.show_demographics()
        
        # Activity patterns
        self.show_activity_patterns()

    def show_demographics(self):
        st.subheader("Audience Demographics")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Age distribution
            age_data = {
                'Age': ['18-24', '25-34', '35-44', '45-54', '55+'],
                'Percentage': [25, 35, 20, 15, 5]
            }
            df_age = pd.DataFrame(age_data)
            fig = px.pie(df_age, values='Percentage', names='Age',
                        title='Age Distribution')
            st.plotly_chart(fig, use_container_width=True)
            
        with col2:
            # Gender distribution
            gender_data = {
                'Gender': ['Male', 'Female', 'Other'],
                'Percentage': [45, 52, 3]
            }
            df_gender = pd.DataFrame(gender_data)
            fig = px.pie(df_gender, values='Percentage', names='Gender',
                        title='Gender Distribution')
            st.plotly_chart(fig, use_container_width=True)

    def show_activity_patterns(self):
        st.subheader("Audience Activity Patterns")
        
        # Example activity data
        hours = list(range(24))
        activity = np.random.normal(100, 30, 24)
        
        df = pd.DataFrame({
            'Hour': hours,
            'Activity': activity
        })
        
        fig = px.line(df, x='Hour', y='Activity',
                     title='Activity by Hour of Day')
        st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    app = SocialMediaAnalytics()
    app.run()
