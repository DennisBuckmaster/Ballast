    
    # Create three columns for the results display
col1, col2, col3 = st.columns([1, 1, 2])
    
with col1:
        st.metric("Weight/Power Ratio", f"{results['wp_ratio']:.1f} lb/hp")
        st.metric("Total Tractor Weight", f"{results['total_weight']:,} lb")
    
with col2:
        st.metric("Front Axle Weight", f"{results['front_axle_weight']:,} lb", 
                  f"{results['front_axle_percentage']}%")
        st.metric("Rear Axle Weight", f"{results['rear_axle_weight']:,} lb", 
                  f"{results['rear_axle_percentage']}%")
    
with col3:
        # Create a visual representation of the weight distribution
        fig = go.Figure()
        
        # Add a bar chart showing the weight distribution
        fig.add_trace(go.Bar(
            x=['Front Axle', 'Rear Axle'],
            y=[results['front_axle_weight'], results['rear_axle_weight']],
            text=[f"{results['front_axle_weight']:,} lb<br>{results['front_axle_percentage']}%", 
                  f"{results['rear_axle_weight']:,} lb<br>{results['rear_axle_percentage']}%"],
            textposition='auto',
            marker_color=['#1E88E5', '#FFC107']
        ))
        
        # Update the layout
        fig.update_layout(
            title='Axle Weight Distribution',
            yaxis_title='Weight (lb)',
            height=300,
            margin=dict(t=30, b=0, l=0, r=0)
        )
        
        # Display the chart
        st.plotly_chart(fig, use_container_width=True)
    
    # Add additional information section
with st.expander("What does this mean?", expanded=True):
        st.markdown(f"""
        ### Tractor Ballast Recommendations
        
        Based on your {tractor_type} tractor with {tractor_power} hp and {implement_mounting} implement:
        
        - **Total weight needed**: Your tractor should weigh approximately **{results['total_weight']:,} lb** for optimal performance.
        - **Front axle**: {results['front_axle_percentage']}% of the weight ({results['front_axle_weight']:,} lb) should be on the front axle.
        - **Rear axle**: {results['rear_axle_percentage']}% of the weight ({results['rear_axle_weight']:,} lb) should be on the rear axle.
        - **Weight/Power ratio**: {results['wp_ratio']:.1f} lb/hp (this indicates how much total weight is needed per horsepower).
        
        ### Why is proper ballasting important?
