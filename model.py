from roboflow import Roboflow


def get_car_damage(url):
    rf = Roboflow(api_key="NySKjChUri3HRW4v37cL")
    project = rf.workspace().project("car-model-dd8rq")
    model = project.version(1).model

    pred= model.predict(url, hosted=True, confidence=15, overlap=30).json()

    result = {}
    scores = []
    Detected_damages = []
    pred_boxes = []
    Total_Number_of_Damages = {}

    if len(pred['predictions']) == 0:
        pass
    else:
        for pr in pred['predictions']:
            scores.append(pr['confidence'])
            Detected_damages.append(pr['class'])
            pred_boxes.append([pr['x'],pr['y'],pr['x']+pr['width'],pr['y']+pr['height']])
        for item in Detected_damages:
            if item in Total_Number_of_Damages:
                Total_Number_of_Damages[item] += 1
            else:
                Total_Number_of_Damages[item] = 1

    result['scores'] = scores
    result['Detected_damages'] = Detected_damages
    result['pred_boxes'] = pred_boxes
    result['Total_Number_of_Damages'] = Total_Number_of_Damages

    print({
        'statusCode': 200,
        'body': result
    })

    # Return it along with the status code of 200 meaning this was succesful 
    return {
        'statusCode': 200,
        'body': result
    }

# print(get_car_damage('https://www.side.cr/wp-content/uploads/2019/09/Car.jpg'))