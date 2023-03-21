import plotly.graph_objects as go
import pandas as pd
import numpy as np
import streamlit as st
from plotly.subplots import make_subplots
import plotly.io as pio
from PyPDF2 import PdfFileReader, PdfFileMerger
import PyPDF2
st. set_page_config(layout="wide")
pio.templates.default = "simple_white"

with open(r"D:\HEM\DSP\Signal-viewer-main\mystyle.css") as design:
    st.markdown(f"<style>{design.read()}</style>", unsafe_allow_html=True)

st.title("Signal Viewer")

link = st.checkbox('link', value=False)
col1, col2 = st.columns([1,2])
col3, col4 = st.columns([1,2])
container1 = st.container()
container2 = st.container()

frames =[]


with container1:

    col1.text("")
    col1.text("")
    file = col1.file_uploader("Upload Files", type={"csv", "txt", "xlsx"})
    signalname1 = col1.text_input("signal 1", value="title",)
    color1 = col1.color_picker( 'Pick A Color', '#00f900',label_visibility="visible",key = "Color 1")
with container2:
    col3.text("")
    col3.text("")
    file2 = col3.file_uploader("Upload Files", type={"csv", "txt", "xlsx"},key = '2nd File')
    signalname2 = col3.text_input("signal 2",value ="title")
    color2 = col3.color_picker( 'Pick A Color', '#00f900',label_visibility="visible",key = "Color 2")
    

if 'read1' not in st.session_state:
            st.session_state['read1'] = 0
if 'read2' not in st.session_state:
            st.session_state['read2'] = 0
if 'read3' not in st.session_state:
            st.session_state['read3'] = 0
    
    


if 'frames' not in st.session_state:
            st.session_state['frames'] = []

if 'frames2' not in st.session_state:
            st.session_state['frames2'] = []
if 'frames3' not in st.session_state:
            st.session_state['frames3'] = []
if 'frames4' not in st.session_state:
            st.session_state['frames4'] = []
            
if 'frames5' not in st.session_state:
            st.session_state['frames5'] = []

if 'frames6' not in st.session_state:
            st.session_state['frames6'] = []
            
if 'frames7' not in st.session_state:
            st.session_state['frames7'] = []
if 'x' not in st.session_state:
        st.session_state['x'] = []
if 'x2' not in st.session_state:
        st.session_state['x2'] = []

if 'y' not in st.session_state:
        st.session_state['y'] = []
if 'y2' not in st.session_state:
        st.session_state['y2'] = []
if 'x_int' not in st.session_state:
    st.session_state['x_int'] = []

if 'y_int' not in st.session_state:
    st.session_state['y_int'] = []


#-----------------------------------------------------------------------------------------

if file is not None and st.session_state['read1'] == 0:
    st.session_state['read1'] = 1
    File = pd.read_csv(file)

    # st.experimental_rerun()

    for f in range(1,500+1):
        st.session_state['x'] = np.array(File.iloc[0:f+1,0])
        st.session_state['y'] = np.array(File.iloc[0:f+1,1])
        
        
        curr_frame = go.Frame( dict(
            data = [go.Scatter(x =  st.session_state['x'], y = st.session_state['y'],mode = "lines",),#update the trace 1 in (1,1)
                    ],
            traces=[0]# the elements of the list [0,1,2] give info on the traces in fig.data
                                    # that are updated by the above three go.Scatter instances
            ))
        st.session_state['frames'].append(curr_frame)
        
#---------------------------------------------------------------------------------------

if file2 is not None and st.session_state['read2'] == 0:
    print(st.session_state['read2'] )
    st.session_state['read2'] = 1
    st.write(type(file2))
    File2 = pd.read_csv(file2)

    # st.experimental_rerun()

    
    for f in range(1,500+1):
        st.session_state['x2'] = np.array(File2.iloc[0:f+1,0])
        st.session_state['y2'] = np.array(File2.iloc[0:f+1,1])
        curr_frame2 = go.Frame( dict(
            data = [go.Scatter(x =  st.session_state['x2'], y = st.session_state['y2'],mode = "lines",)#update the trace 1 in (1,1)
                    ],
            traces=[0] # the elements of the list [0,1,2] give info on the traces in fig.data
                                    # that are updated by the above three go.Scatter instances
            ))
        st.session_state['frames2'].append(curr_frame2)
        
#---------------------------------------------------------------------------------------


if link == False:

    
    figure = go.Figure(
        frames = [fr.update(
            layout={
                "xaxis": {"range": [max(fr.data[0].x) - 1, max(fr.data[0].x)]},
                "yaxis": {"range": [min(fr.data[0].y), max(fr.data[0].y)]}
            }
        )for fr in st.session_state['frames']]
        )
    figure.update_layout(width=600, height=475)


    figure.update_layout(showlegend=True,title=dict(text="Graph #1"), 
                        xaxis={
                            'showgrid':False,
                            'linecolor':'#000000',
                            
                            'ticks':'outside',
                            'showline':True
                        },
                        updatemenus=[dict(buttons = [dict(
                                               args = [None, {"frame": {"duration": 200, 
                                                                        "redraw": True},
                                                              "fromcurrent": True, 
                                                              "transition": {"duration": 0}}],
                                               label = "Play",
                                               method = "animate"),dict(
                                               args = [None, {"frame": {"duration": 50, 
                                                                        "redraw": True},
                                                              "fromcurrent": True, 
                                                              "transition": {"duration": 0}}],
                                               label = "Play X2",
                                               method = "animate"),dict(
                                               args = [None, {"frame": {"duration": 200, 
                                                                        "redraw": True},
                                                              "fromcurrent": False, 
                                                              "transition": {"duration": 0}}],
                                               label = "Start over",
                                               method = "animate"),dict(
                                               args = [[None], {"frame": {"duration": 0, "redraw": False},
                                                                "mode": "immediate",
                                                                "transition": {"duration": 0}}],
                                               label = "Pause",
                                               method = "animate"),
                                               dict(
                                                args=[None, {"frame": {"duration": 50, "redraw": True},
                                                            "fromcurrent": False, "transition": {"duration": 0},
                                                            "mode": "immediate"}],
                                                label="Rewind",
                                                method="animate"
)],
                                type='buttons',
                                showactive=False,
                                xanchor='right',
                                yanchor='top')]
                        )

    figure.add_trace(go.Scatter(x =st.session_state['x_int'], y = st.session_state['y_int'],mode = "lines",line=dict(color=color1),name=signalname1),)


    

    if file is not None:
        with container1:
            col2.write(figure)
            plot=go.Figure(go.Scatter(x =st.session_state['x'], y = st.session_state['y'],mode = "lines",line=dict(color=color1)))
            col1.button('Save as PDF file', on_click=plot.write_image("D:\HEM\DSP\Signal-viewer-main/fig1.pdf"))
            df = pd.DataFrame(st.session_state['y'])
            table = go.Figure(data=[go.Table(header=dict(values=['Plot', 'Mean','std','duration','max','min']),
                            cells=dict(values=['figure 1',df.mean(),df.std(),max(st.session_state['x']),max(df),min(df)]))
            ])
            table.write_image("D:\HEM\DSP\Signal-viewer-main/Stats1.pdf")
            merger = PyPDF2.PdfFileMerger(strict=True)
            f1 = PdfFileReader(open('fig1.pdf', 'rb'))
            f2 = PdfFileReader(open('Stats1.pdf', 'rb'))
            
            merger = PdfFileMerger(strict=True)

            merger.append(f1)
            merger.append(f2)
            

            merger.write('CompleteGraph1.pdf')
#--------------------------------------------------------------------------------------

    figure2 = go.Figure(
        frames = [fr.update(
            layout={
                "xaxis": {"range": [max(fr.data[0].x) - 1, max(fr.data[0].x)]},
                "yaxis": {"range": [min(fr.data[0].y), max(fr.data[0].y)]}
            }
        )for fr in st.session_state['frames2']]
        )
    figure2.update_layout(width=600, height=475)


    figure2.update_layout(showlegend=True,title=dict(text="Graph #2"), 
                        xaxis={
                            'showgrid':False,
                            'linecolor':'#000000',
                            
                            'ticks':'outside',
                            'showline':True
                        },
                        updatemenus=[dict(buttons = [dict(
                                               args = [None, {"frame": {"duration": 200, 
                                                                        "redraw": True},
                                                              "fromcurrent": True, 
                                                              "transition": {"duration": 0}}],
                                               label = "Play",
                                               method = "animate"),dict(
                                               args = [None, {"frame": {"duration": 50, 
                                                                        "redraw": True},
                                                              "fromcurrent": True, 
                                                              "transition": {"duration": 0}}],
                                               label = "Play X2",
                                               method = "animate"),dict(
                                               args = [None, {"frame": {"duration": 200, 
                                                                        "redraw": True},
                                                              "fromcurrent": False, 
                                                              "transition": {"duration": 0}}],
                                               label = "Start over",
                                               method = "animate"),dict(
                                               args = [[None], {"frame": {"duration": 0, "redraw": False},
                                                                "mode": "immediate",
                                                                "transition": {"duration": 0}}],
                                               label = "Pause",
                                               method = "animate"),
                                               dict(
                                                args=[None, {"frame": {"duration": 50, "redraw": True},
                                                            "fromcurrent": False, "transition": {"duration": 0},
                                                            "mode": "immediate"}],
                                                label="Rewind",
                                                method="animate"
)],
                                type='buttons',
                                showactive=False,
                                xanchor='right',
                                yanchor='top')]
                        )

    figure2.add_trace(go.Scatter(x =st.session_state['x_int'], y = st.session_state['y_int'],mode = "lines",line=dict(color=color2),name=signalname2),)
    

    if file2 is not None:
        with container2:
            col4.write(figure2)
        
            plot2=go.Figure(go.Scatter(x =st.session_state['x2'], y = st.session_state['y2'],mode = "lines",line=dict(color=color1)))
            col3.button('Save as PDF file(2)', on_click=plot2.write_image("D:\HEM\DSP\Signal-viewer-main/fig2.pdf"))
            df = pd.DataFrame(st.session_state['y2'])
            table2 = go.Figure(data=[go.Table(header=dict(values=['Plot', 'Mean','std','duration','max','min']),
                            cells=dict(values=['stats2',df.mean(),df.std(),max(st.session_state['x2']),max(df),min(df)]))
            ])
            table2.write_image("D:\HEM\DSP\Signal-viewer-main/Stats2.pdf")
            merger = PyPDF2.PdfFileMerger(strict=True)
            f1 = PdfFileReader(open('fig2.pdf', 'rb'))
            f2 = PdfFileReader(open('Stats2.pdf', 'rb'))
            
            merger = PdfFileMerger(strict=True)

            merger.append(f1)
            merger.append(f2)
            

            merger.write('CompleteGraph2.pdf')


#--------------------------------------------------------------------------------------
j=-1
i = -1
if link ==True:
    if st.session_state['read3'] == 2:
        del st.session_state['frames3']
        st.session_state['frames3'] = []

    if st.session_state['read3'] != 2:
        st.session_state['read3'] =2


    for fr in st.session_state['frames2']:  
        
        st.session_state['frames4'].append(fr.data[0].x)
        st.session_state['frames5'].append(fr.data[0].y)
        j=j+1
    
    if len(st.session_state['frames2'])>1 and len(st.session_state['frames'])>1:    
        for fr in  st.session_state['frames']:
                st.session_state['frames6'].append(fr.data[0].x)
                st.session_state['frames7'].append(fr.data[0].y)
                curr_frame = go.Frame( dict(
                data = [go.Scatter(x =  st.session_state['frames6'][i], y = st.session_state['frames7'][i],mode = "lines",),#update the trace 1 in (1,1)
                        go.Scatter(x =  st.session_state['frames4'][i], y = st.session_state['frames5'][i],mode = "lines",)
                        ],
                traces=[0,1]# the elements of the list [0,1] give info on the traces in fig.data
                                        # that are updated by the above three go.Scatter instances
                ))
                i=i+1
                st.session_state['frames3'].append(curr_frame)

    if len(st.session_state['frames2'])<1 and len(st.session_state['frames'])>1:    
        for fr in  st.session_state['frames']:
                st.session_state['frames6'].append(fr.data[0].x)
                st.session_state['frames7'].append(fr.data[0].y)
                curr_frame = go.Frame( dict(
                data = [go.Scatter(x =  st.session_state['frames6'][i], y = st.session_state['frames7'][i],mode = "lines",),#update the trace 1 in (1,1)
                        ],
                traces=[0]# the elements of the list [0] give info on the traces in fig.data
                                        # that are updated by the above three go.Scatter instances
                ))
                i=i+1
                st.session_state['frames3'].append(curr_frame)
    
    if len(st.session_state['frames2'])>1 and len(st.session_state['frames'])<1:    
        for fr in  st.session_state['frames2']:
                curr_frame = go.Frame( dict(
                data = [
                        go.Scatter(x =  st.session_state['frames4'][i], y = st.session_state['frames5'][i],mode = "lines",)
                        ],
                traces=[1]# the elements of the list [1] give info on the traces in fig.data
                                        # that are updated by the above three go.Scatter instances
                ))
                j=j+1
                st.session_state['frames3'].append(curr_frame)

    frames5 = [fr.update(
        layout={
            "xaxis": {"range": [max(fr.data[0].x) - 1, max(fr.data[0].x)]},
            "yaxis": {"range": [-1,1]}
        }
    )for fr in st.session_state['frames3']]
           
                       
    fig = make_subplots(rows=2, cols=1, subplot_titles = ('Graph #1', 'Graph #2'),shared_xaxes='all',shared_yaxes='all')
    fig.add_trace(go.Scatter(x =st.session_state['x_int'], y = st.session_state['y_int'],mode = "lines",line=dict(color=color1),name = signalname1), row=1, col=1);
    fig.add_trace(go.Scatter(x =st.session_state['x_int'], y = st.session_state['y_int'],mode = "lines",line=dict(color=color2),name = signalname2), row=2, col=1);
    fig.update_layout(showlegend=True,width=600, height=475)
    fig.update_yaxes(range=[0, 9]);#this line updates both yaxis, and yaxis2 range


    updatemenus=annotations=[dict(buttons = [dict(
                                               args = [None, {"frame": {"duration": 200, 
                                                                        "redraw": True},
                                                              "fromcurrent": True, 
                                                              "transition": {"duration": 0}}],
                                               label = "Play",
                                               method = "animate"),dict(
                                               args = [None, {"frame": {"duration": 50, 
                                                                        "redraw": True},
                                                              "fromcurrent": True, 
                                                              "transition": {"duration": 0}}],
                                               label = "Play X2",
                                               method = "animate"),dict(
                                               args = [None, {"frame": {"duration": 200, 
                                                                        "redraw": True},
                                                              "fromcurrent": False, 
                                                              "transition": {"duration": 0}}],
                                               label = "Start over",
                                               method = "animate"),dict(
                                                args = [[None], {"frame": {"duration": 0, "redraw": False},
                                                                    "mode": "immediate",
                                                                    "transition": {"duration": 0}}],
                                                label = "Pause",
                                                method = "animate"),
                                               dict(
                                                args=[None, {"frame": {"duration": 50, "redraw": True},
                                                            "fromcurrent": False, "transition": {"duration": 0},
                                                            "mode": "immediate"}],
                                                label="Rewind",
                                                method="animate"
)],
                                type='buttons',
                                showactive=False,
                                xanchor='right',
                                yanchor='top')]
                        


    fig.update(frames=frames5),
    fig.update_layout(updatemenus=updatemenus,
                    );
    

    col2.write(fig)
    figpdf = make_subplots(rows=2, cols=1, subplot_titles = ('Graph #1', 'Graph #2'),shared_xaxes='all',shared_yaxes='all')
    figpdf.add_trace(go.Scatter(x =st.session_state['frames6'][i], y = st.session_state['frames7'][i],mode = "lines",line=dict(color=color1),name = signalname1), row=1, col=1);
    figpdf.add_trace(go.Scatter(x =st.session_state['frames4'][j], y =st.session_state['frames5'][j],mode = "lines",line=dict(color=color2),name = signalname2), row=2, col=1);
    
        
    col1.button('Save as PDF file', on_click=figpdf.write_image("D:\HEM\DSP\Signal-viewer-main/figSubplots.pdf"))
    if len(st.session_state['frames2'])>1 and len(st.session_state['frames'])>1: 
       
        dfPlot2 = pd.DataFrame(st.session_state['frames5'][j])
        dfPlot1 = pd.DataFrame(st.session_state['frames7'][i])
        table = go.Figure(data=[go.Table(header=dict(values=['Plot', 'Mean','std','duration','max','min']),
                            cells=dict(values=[['figure 1','figure 2'],[dfPlot1.mean(),dfPlot2.mean()],[dfPlot1.std(),dfPlot2.std()],[max(st.session_state['frames6'][i]),max(st.session_state['frames4'][i])],[max(dfPlot1),max(dfPlot2)],[min(dfPlot1),min(dfPlot2)]]
                                            ))
            ])
        table.write_image("D:\HEM\DSP\Signal-viewer-main/StatsSubplots.pdf")
        merger = PyPDF2.PdfFileMerger(strict=True)
        f1 = PdfFileReader(open('figSubplots.pdf', 'rb'))
        f2 = PdfFileReader(open('StatsSubplots.pdf', 'rb'))
        
        merger = PdfFileMerger(strict=True)

        merger.append(f1)
        merger.append(f2)
        

        merger.write('CompleteGraphSubplots.pdf')