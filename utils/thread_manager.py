#!/usr/bin/env python3
# Thread Management

import threading
import time
from queue import Queue

class ThreadManager:
    def __init__(self, max_threads=10):
        self.max_threads = max_threads
        self.threads = []
        self.task_queue = Queue()
        self.running = True
        
    def add_task(self, task_func, *args, **kwargs):
        """إضافة مهمة للتنفيذ"""
        self.task_queue.put((task_func, args, kwargs))
        
    def worker(self):
        """عامل لمعالجة المهام"""
        while self.running:
            try:
                task_func, args, kwargs = self.task_queue.get(timeout=1)
                task_func(*args, **kwargs)
                self.task_queue.task_done()
            except:
                time.sleep(0.1)
                
    def start(self):
        """بدء مدير الخيوط"""
        for _ in range(self.max_threads):
            thread = threading.Thread(target=self.worker, daemon=True)
            thread.start()
            self.threads.append(thread)
            
    def stop(self):
        """إيقاف جميع الخيوط"""
        self.running = False
        for thread in self.threads:
            thread.join(timeout=1)
