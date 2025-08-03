# test_faiss.py
try:
    import faiss
    print("FAISS imported successfully!")
except ImportError as e:
    print("Error importing FAISS:", e)
