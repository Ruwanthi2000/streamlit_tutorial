import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import graphviz as graphviz

rand=np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)#color ="pink"
st.pyplot(fig)

import streamlit as st
import pandas as pd
import numpy as np
df= pd.DataFrame(    
    np.random.randn(10, 2),    
    columns=['x', 'y'])
st.line_chart(df)

import streamlit as st
import pandas as pd
import numpy as np
df= pd.DataFrame(    
    np.random.randn(10, 2),    
    columns=['x', 'y'])
st.bar_chart(df)

import streamlit as st
import pandas as pd
import numpy as np
df= pd.DataFrame(    
    np.random.randn(10, 2),    
    columns=['x', 'y'])
st.area_chart(df)

import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

df = pd.DataFrame(   
    np.random.randn(500, 3),   
    columns=['x','y','z'])

c = alt.Chart(df).mark_circle().encode(   
    x='x' , y='y' , size='z', color='z', tooltip=['x', 'y', 'z'])

st.altair_chart(c, use_container_width=True)



st.graphviz_chart('''    
    digraph {        
        Big_shark -> Tuna        
        Tuna -> Mackerel        
        Mackerel -> Small_fishes        
        Small_fishes -> Shrimp    
    }
''')


df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [37.76, -122.4],
columns=['lat', 'lon'])
st.map(df)