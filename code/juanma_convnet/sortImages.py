import os, shutil

# Script in charge of placing images into their corresponding directory


source_dir = '/convnet/brazilian_coffee_scenes'
base_dir = '/convnet/coffe_images'

# Base directory located at /convnet/base_dir
os.mkdir(base_dir)

train_dir = os.path.join(base_dir, 'train')
os.mkdir(train_dir)

validation_dir = os.path.join(base_dir,'validation')
os.mkdir(validation_dir)

test_dir = os.path.join(base_dir,'test')
os.mkdir(test_dir)

train_coffe_fields = os.path.join(train_dir, 'coffe_fields')
os.mkdir(train_coffe_fields)

train_non_coffe_fields = os.path.join(train_dir, 'non_coffe_fields')
os.mkdir(train_non_coffe_fields)

validation_coffe_fields = os.path.join(validation_dir, 'coffe_fields')
os.mkdir(validation_coffe_fields)

validation_non_coffe_fields = os.path.join(validation_dir, 'non_coffe_fields')
os.mkdir(validation_non_coffe_fields)

# First approach with train, validation and test data

# Create test set
for i in range(1,4):
    # Iterate over folds and copy content to train set
    curr_train_dir = os.path.join(source_dir,'fold'+str(i))
    files = os.listdir(curr_train_dir)
    j = 0
    for file in files:
        curr_file = os.path.join(curr_train_dir,file)
        if(j < 300):
            shutil.copy(curr_file, train_coffe_fields)
        else:
            shutil.copy(curr_file, train_non_coffe_fields)
        j +=1

# Create validation set

val_src_dir = os.path.join(source_dir,'fold4')
files = os.listdir(val_src_dir)
j = 0
for file in files:
    curr_file = os.path.join(val_src_dir,file)
    if(j < 300):
        shutil.copy(curr_file, validation_coffe_fields)
    else:
        shutil.copy(curr_file, validation_non_coffe_fields)
    j +=1
    