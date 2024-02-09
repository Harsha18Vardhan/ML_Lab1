def Eucledian_Distance(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Vector Should be of same Dimensions")
    else:
        sum =0 
        for i in range(len(vector1)):
            sum += (vector1[i]-vector2[i])**2
        return sum**0.5
    
def manhattan_distance(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Vector Should be of same Dimensions")
    else:
        sum = 0
        for i in range(len(vector1)):
            sum += abs(vector1[i] - vector2[i])
        return sum
    
vectorA= [int(x) for x in input('Enter vector A seperated by commas:').split(',')]
vectorB= [int(x) for x in input('Enter vector B seperated by commas:').split(',')]

Euclidian_result=Eucledian_Distance(vectorA, vectorB)        
manhattan_result=manhattan_distance(vectorA, vectorB)

print("Euclidian distance is ",Euclidian_result)
print("Manhattan distance is ",manhattan_result)

def K_nearest_neighbors(k,data_points):
    distances= []
    for i in range(1, len(data_points)):
        Calculated_Distance = Eucledian_Distance(data_points[0], data_points[i])
        distances.append((Calculated_Distance, data_points[i][2]))
    
    for j in range(len(distances)):
        for l in range(0, len(distances) - j - 1):
            if distances[l][0] > distances[l+1][0]:
                distances[l], distances[l+1] = distances[l+1], distances[l]
    
    k_nearest = distances[:k]
    
    frequency_class1= 0
    for distance, label in k_nearest:
        if label == 1:
            frequency_class1 += 1
            
    frequency_class2= k -frequency_class1
    
    if frequency_class1 > frequency_class2:
        return "Belongs to the first class"
    else:
        return "Belongs to second class"
    
def Encode_Labels(labels):
    unique_label_set = set(labels)
    label_to_code = {}
    code = 0
    
    for label in unique_label_set:
        label_to_code[label] = code
        code += 1
    
    for label in labels:
        encoded_label = label_to_code[label]
        
    return encoded_label, label_to_code

def One_hot_encode(labels):
    unique_labels= sorted(set(labels))
    one_hot_encoding = {}
    
    for label in unique_labels:
        one_hot_encoding[label] = [0] * len(unique_labels)
    
    for i, label in enumerate(unique_labels):
        one_hot_encoding[label][i] = 1
    encoded_labels = []
    for label in labels:
        one_hot_encoding[label]
        
    return encoded_labels, one_hot_encoding
    
def read_arff_file(file_path):
    with open(file_path, 'r') as f:
        text = f.readline()
    
    Attributes = []
    Data = []
    Labels = []
    read_data = False

    for line in text:
        line = text.strip()

        if not line or text.startswith('%'):
            continue
        
        if line.lower().startswith('@attribute'):
            attribute_name = line.split()[1]
            Attributes.append(attribute_name)
        
        elif line.lower().startswith('@data'):
            read_data = True
        
        elif read_data:
            Data.append(line.split(','))
        
        elif line.lower().startswith('@relation'):
            relation_name = line.split()[1]
        
        elif line.lower().startswith('{'):
            Labels.extend(line.strip('{}').split(','))
    
    return Data, Attributes, Labels



file_path = "stackex_coffee.arff"
Data, Attributes, Labels = read_arff_file(file_path)

coordinates = []
for row in Data: 
    for value in row[:-1]:
        featured_value = float(value)
        tuple(featured_value)
        label = int(row[-1])

        coordinates.append((featured_value, label))


k = int(input("Enter a certain value of k = "))
read_arff_file("stackex_coffee.arff")
result = K_nearest_neighbors(k, coordinates)
print("Classification result:", result)