#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import psutil
def activeconnectionsfunc():
    def get_active_connections():
        connections = psutil.net_connections()
    
        active_connections = []
        for conn in connections:
            if conn.status == 'ESTABLISHED':
                active_connections.append(conn)
    
        return active_connections
    
    
    # Example usage
    active_connections = get_active_connections()
    
    if active_connections:
        print("Active Connections:")
        for conn in active_connections:
            print(f"Local Address: {conn.laddr.ip}:{conn.laddr.port}")
            print(f"Remote Address: {conn.raddr.ip}:{conn.raddr.port}")
            print("---")
    else:
        print("No active connections found.")
    
