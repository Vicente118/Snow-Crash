There is 32 bits binary (SUID bit is set again):
```C
int32_t afterSubstr(char* inputString, int32_t compareValue)
{
    int32_t matchFound = 0;
    char* currentPtr = inputString;
    void* comparePtr;
    
    while (*currentPtr != 0)
    {
        matchFound = 1;
        comparePtr = nullptr;
        
        while (matchFound == 1)
        {
            if (*(comparePtr + compareValue) == 0)
                break;
            
            if (*(comparePtr + compareValue) != *(comparePtr + currentPtr))
                matchFound = 0;
            
            comparePtr += 1;
        }
        
        if (matchFound == 1)
            break;
        
        currentPtr = &currentPtr[1];
    }
    
    if (matchFound != 0)
        return comparePtr + currentPtr;
    
    return 0;
}


int32_t isLib(char* pathString, int32_t libNameToFind)
{
    char* foundPosition = afterSubstr(pathString, libNameToFind);
    
    if (foundPosition == 0)
        return 0;
    
    if (*foundPosition != 0x2d)
        return 0;
    
    int32_t hasDigits = 0;
    void* currentChar = &foundPosition[1];
    
    while (*currentChar s> 0x2f)
    {
        if (*currentChar s> 0x39)
            break;
        
        hasDigits = 1;
        currentChar += 1;
    }
    
    if (hasDigits == 0 || *currentChar != 0x2e)
        return 0;
    
    int32_t hasMoreDigits = 0;
    void* nextChar = currentChar + 1;
    
    while (*nextChar s> 0x2f)
    {
        if (*nextChar s> 0x39)
            break;
        
        hasMoreDigits = 1;
        nextChar += 1;
    }
    
    if (hasMoreDigits == 0)
        return 0;
    
    void* compareCharPtr = nullptr;
    
    while (true)
    {
        if (*(compareCharPtr + end.3170) == 0)
            return 1;
        
        if (*(compareCharPtr + end.3170) != *(compareCharPtr + nextChar))
            break;
        
        compareCharPtr += 1;
    }
    
    return 0;
}


int32_t main(int32_t argc, char** argv, char** envp)
{
    void* gsbase;
    int32_t stackCanary = *(gsbase + 0x14);
    int32_t libcFound = 0;
    void* counter = 0xffffffff;
    void* result;
    
    if (ptrace(request: PTRACE_TRACEME, 0, 1, 0) s>= 0)
    {
        if (getenv(name: "LD_PRELOAD") == 0)
        {
            if (open(file: "/etc/ld.so.preload", oflag: 0) s<= 0)
            {
                int32_t mapsFileDesc = syscall_open("/proc/self/maps", 0);
                
                if (mapsFileDesc != 0xffffffff)
                {
                    while (true)
                    {
                        void lineBuf;
                        result = syscall_gets(&lineBuf, 0x100, mapsFileDesc);
                        
                        if (result == 0)
                            break;
                        
                        if (isLib(&lineBuf, "libc") != 0)
                            libcFound = 1;
                        else if (libcFound != 0)
                        {
                            if (isLib(&lineBuf, &data_8048c30) != 0)
                            {
                                if (argc != 2)
                                {
                                    result = fwrite(buf: "You need to provied only one arg…", size: 1, count: 0x22, fp: stderr);
                                }
                                else
                                {
                                    while (true)
                                    {
                                        counter += 1;
                                        int32_t stringLength = 0xffffffff;
                                        int32_t argPtr = argv[1];
                                        
                                        while (stringLength != 0)
                                        {
                                            bool charExists = 0 != *argPtr;
                                            argPtr += 1;
                                            stringLength -= 1;
                                            
                                            if (not(charExists))
                                                break;
                                        }
                                        
                                        if (counter u>= not.d(stringLength) - 1)
                                            break;
                                        
                                        putchar(c: sx.d(*(counter + argv[1])) + counter);
                                    }
                                    
                                    result = fputc(c: 0xa, fp: stdout);
                                }
                                
                                break;
                            }
                            
                            if (afterSubstr(&lineBuf, "00000000 00:00 0") == 0)
                            {
                                result = fwrite(buf: "LD_PRELOAD detected through memo…", size: 1, count: 0x30, fp: stderr);
                                break;
                            }
                        }
                    }
                }
                else
                {
                    fwrite(buf: "/proc/self/maps is unaccessible,…", size: 1, count: 0x46, fp: stderr);
                    result = 1;
                }
            }
            else
            {
                fwrite(buf: "Injection Linked lib detected ex…", size: 1, count: 0x25, fp: stderr);
                result = 1;
            }
        }
        else
        {
            fwrite(buf: "Injection Linked lib detected ex…", size: 1, count: 0x25, fp: stderr);
            result = 1;
        }
    }
    else
    {
        puts(str: "You should not reverse this");
        result = 1;
    }
    
    if (stackCanary == *(gsbase + 0x14))
        return result;
    
    __stack_chk_fail();
    noreturn;
}
```