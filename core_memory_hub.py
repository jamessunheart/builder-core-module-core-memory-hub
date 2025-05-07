import datetime

class CoreMemoryHub:
    """
    Stores and manages long-term structured memory for Builder Core.
    Allows insertion, retrieval, and summarization of key events.
    Supports redundancy, with future consolidation into canonical truths.
    """

    def __init__(self):
        self.memories = []

    def remember(self, entry, tags=None):
        self.memories.append({
            "timestamp": datetime.datetime.utcnow().isoformat(),
            "entry": entry,
            "tags": tags or []
        })

    def recall(self, tag_filter=None):
        if not tag_filter:
            return self.memories[-5:]  # most recent 5
        return [m for m in self.memories if any(tag in m['tags'] for tag in tag_filter)][-5:]

    def summarize_recent(self, count=5):
        return [m['entry'] for m in self.memories[-count:]]

    def consolidate(self):
        # Future: deduplicate, merge, and create canonical truths
        return {"summary": "Consolidation function is a placeholder for future optimization."}
