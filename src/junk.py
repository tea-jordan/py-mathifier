with tokenize.open(FILE_NAME) as f:
        tokens = tokenize.generate_tokens(f.readline)
        
        tokens_list = list(tokens)
        
        modifications = []
        
        # Find the string token 'hello' and change it to 'world'
        for i, token in enumerate(tokens_list):
            
            #print("General Token Info:")
            #print(f"\t{token}")
            #print(f"\tString: {token.string}")
            #print(f"\tIs String DataType: {isinstance(token.string, str)}")
            #print(f"Token Exact Type: {token.exact_type}\n")
            
            """
            
            
            new_string = "AYO"
            
            # Create a new TokenInfo with the updated string
            new_token = tokenize.TokenInfo(
                type=token.type,
                string=new_string,
                start=token.start,
                end=token.end,
                line=token.line
            )
            tokens_list[i] = new_token
            """
            
            # TODO: add logic to only add one mod / line, in case of multiple uses on one line
            if tokens_list[i].exact_type == 1 and tokens_list[i].string == "my_var": #main
                
                modifications.append(
                    {
                        'type': Modification.RENAME,
                        'line': tokens_list[i].start[0],
                        'start': tokens_list[i].start,
                        'end_char': tokens_list[i].start[1]
                    }
                )
                """
                # Create a new TokenInfo with the updated string
                new_token = tokenize.TokenInfo(
                    type=token.type,
                    string="merge_sort",
                    start=token.start,
                    end=token.end,
                    line=token.line
                )
                tokens_list[i] = new_token
                """
            
            print(tokens_list[i])
        










        for i, token in enumerate(tokens_list):
        
        if tokens_list[i].exact_type == type_condition and tokens_list[i].string == text_condition: #1, my_var
        
            if tokens_list[i].start[0] in mod_dict.keys():
                mod_dict[tokens_list[i].start[0]].append(
                    {
                    'type': mod_type,
                    'line': tokens_list[i].start[0],
                    'start': tokens_list[i].start,
                    'start_char': tokens_list[i].start[1],
                    'end': tokens_list[i].end, 
                    'end_char': tokens_list[i].end[1], 
                    'text':""
                    }
                )
            else:
                mod_dict[tokens_list[i].start[0]] = [{
                    'type': mod_type,
                    'line': tokens_list[i].start[0],
                    'start': tokens_list[i].start,
                    'start_char': tokens_list[i].start[1],
                    'end': tokens_list[i].end, 
                    'end_char': tokens_list[i].end[1]
                }]
 
    return [mod_dict[i] for i in mod_dict]