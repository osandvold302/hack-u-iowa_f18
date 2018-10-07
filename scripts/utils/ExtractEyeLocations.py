import pandas as pd

X_INDEX = 2
Y_INDEX = 3
Z_INDEX = 4

def getEyeLocation(file_path):
    df = pd.read_csv(file_path, comment='#')

    left_eye_location = []
    right_eye_location = []

    for index in df.itertuples():
        #Find location of Left Eye
        if(index[1] == "LE"):
            left_eye_location.append(index[X_INDEX]) # x coordinate
            left_eye_location.append(index[Y_INDEX]) # y coordinate
            left_eye_location.append(index[Z_INDEX]) # z coordinate
        #Find location of Right Eye
        if(index[1] == "RE"):
            right_eye_location.append(index[X_INDEX]) # x coordinate
            right_eye_location.append(index[Y_INDEX]) # y coordinate
            right_eye_location.append(index[Z_INDEX]) # z coordinate
    left_eye_right_eye = (left_eye_location, right_eye_location)

    # Returns a tuple.
    # First element is the location of the left eye in array form (x,y,z).
    # Second element is the location of the right eye in array form (x,y,z).
    return left_eye_right_eye


