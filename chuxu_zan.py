from zhihu import ZhihuClient
import zhihu



Cookies_File = 'cookies.json'

client = ZhihuClient(Cookies_File)

url = 'https://www.zhihu.com/people/yanyang1025'
author = client.author(url)


print('取用户粉丝数 %d' % author.follower_num)
print('用户得到赞同数 %d' % author.upvote_num)


for act in author.activities:
   if act.type == zhihu.ActType.UPVOTE_ANSWER:
       print('%s 在 %s 赞同了问题 %s 中 %s(motto: %s) 的回答, '
             '此回答赞同数 %d' %
             (author.name, act.time, act.answer.question.title,
              act.answer.author.name, act.answer.author.motto,
              act.answer.upvote_num))


#for question in author.followed_questions:
#    print(question.title)

