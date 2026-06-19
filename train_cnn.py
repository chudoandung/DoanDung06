import os  
import tensorflow as tf

layers = tf.keras.layers
models = tf.keras.models


BATCH_SIZE = 8
IMG_HEIGHT = 150
IMG_WIDTH = 150
DATASET_DIR = "dataset"

if not os.path.exists(DATASET_DIR):
    print(f"⚠️ Vui lòng tạo thư mục '{DATASET_DIR}' và phân loại ảnh diễn viên!")
else:
    train_ds = tf.keras.utils.image_dataset_from_directory(
        DATASET_DIR,
        validation_split=0.2,
        subset="training",
        seed=123,
        image_size=(IMG_HEIGHT, IMG_WIDTH),
        batch_size=BATCH_SIZE
    )

    val_ds = tf.keras.utils.image_dataset_from_directory(
        DATASET_DIR,
        validation_split=0.2,
        subset="validation",
        seed=123,
        image_size=(IMG_HEIGHT, IMG_WIDTH),
        batch_size=BATCH_SIZE
    )

    class_names = train_ds.class_names
    print("🎯 Danh sách diễn viên hệ thống sẽ học:", class_names)

    AUTOTUNE = tf.data.AUTOTUNE
    train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
    val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
    

    num_classes = len(class_names)
    print(f"🎯 Tổng số diễn viên thực tế hệ thống đếm được: {num_classes}")

    model = models.Sequential([
        tf.keras.layers.Input(shape=(IMG_HEIGHT, IMG_WIDTH, 3)),
        tf.keras.layers.Rescaling(1./255),
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        
        tf.keras.layers.Dense(num_classes) 
    ])

    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])

    print("🚀 Đang chạy training mô hình CNN...")
    model.fit(train_ds, validation_data=val_ds, epochs=15)

    model.save(r"D:\destop 15092021\CSI08\SPCK\actor_cnn_model.keras")
    with open(r"D:\destop 15092021\CSI08\SPCK\actor_labels.txt", "w", encoding="utf-8") as f:
        for name in class_names:
            f.write(name + "\n")
            
    print("✅ Đã train xong! File 'actor_cnn_model.keras' đã sẵn sàng.")