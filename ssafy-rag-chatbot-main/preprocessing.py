# 데이터 소스 경로
import json
import os

def load_json_files_and_merge(base_directory):
    all_data = []
    # 디렉토리 내의 모든 JSON 파일 순회
    for filename in os.listdir(base_directory):
        if filename.endswith('.json'):
            file_path = os.path.join(base_directory, filename)
            
            # JSON 파일 읽기
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

                if 'SJML' in data and 'text' in data['SJML']:
                    for text_item in data['SJML']['text']:
                        all_data.append(text_item)
                
            # 데이터 리스트에 추가
            all_data.append(data)
    
    return all_data


if __name__ == "__main__":
    base_directory = 'data'

    # 데이터 로드 및 병합 (이 부분을 크롤링으로 대체해도 좋습니다)
    merged_data_list = load_json_files_and_merge(base_directory)

    print(len(merged_data_list))
    print(merged_data_list[0])