# Signal-viewer

Develop a web application that illustrates multi-channel signal viewer that has the following features:
- The user can browse his PC to open any signal file. Each group will need to provide samples from three different 
medical signals (e.g. ECG, EMG, EEG,…etc). Each signal type should have an example for normal signal and abnormal 
signal.
- Your application should contain two main identical graphs. The user can open different signals in each graph. i.e. each 
graph has to have its own controls. The user can run each graph independently or link both graphs via a button in the 
UI. When the graphs are linked, the two graphs must display the same time frames, signal speed, and same viewport if 
zoomed or panned (i.e. if the user zoom on one graph, the other graph should apply the same exact zoom as well). If 
the link of the two graphs is disabled, then each graph can run its signals independently.
- In any of the two graphs, when the user opens a signal file, the signal should show up in the cine mode (i.e. a running 
signal through time, similar to the one you see in the ICU monitors). Do NOT open a signal in a static mode. If the 
signal ends, there should be a rewind option to either stop the signal or start running it again from the beginning.
- The use can manipulate the running signals through UI elements that provide the below function:
• Change color,
• Add a label/title for each signal,
• Show/hide,
• Control/customize the cine speed,
• Zoom in/out,
• Pause/play/rewind(on/off),
• Scroll/Pan the signal in any direction (left, top, right, bottom). Scroll is performed through sliders, and pan is
performed through the mouse movements.
