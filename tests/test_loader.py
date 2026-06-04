from src.data_loader.loader import (
    load_data,
    generate_metadata,
    save_metadata,
    generate_dataset_summary,
    save_dataset_summary,
    get_valid_states,
    get_valid_crops
)

df = load_data()

metadata = generate_metadata(df)
save_metadata(metadata)

summary = generate_dataset_summary(df)
save_dataset_summary(summary)

VALID_STATES = get_valid_states(df)
VALID_CROPS = get_valid_crops(df)

print(df.shape)
print(len(VALID_STATES))
print(len(VALID_CROPS))