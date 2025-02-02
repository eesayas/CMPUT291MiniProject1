 -- Data prepared by Vincent Wainman, vwainman@ualberta.ca, published on 2020-09-28 and revised on 2020-10-06

PRAGMA foreign_keys = ON;

insert into users values ('u001','Vince Wain', '123', 'Edmonton', '2019-01-05');
insert into users values ('u002','George', '123','Regina', '2019-01-06');
insert into users values ('u003','Martha', '123','Toronto', '2019-01-10');
insert into users values ('u004','Donald Comb', '123','Edmonton', '2019-01-15');
insert into users values ('u005','Jane Doe', '123','Regina', '2019-02-03'); 
insert into users values ('u006','John Doe', '123','Regina', '2019-02-03');
insert into users values ('u007','Mark Burger', '123','Toronto', '2019-03-04');
insert into users values ('u008','Stevey Manny', '123','Calgary', '2019-03-05');
insert into users values ('u009','Barney Barns', '123','Calgary', '2019-03-06');
insert into users values ('u010','Jane Doe', '123','Ottawa', '2019-03-08');
insert into users values ('u011','Lily Ford', '123','Regina', '2019-06-03'); 
insert into users values ('u012','Joe Butters', '123','Regina', '2019-06-03');
insert into users values ('u013','Henry', '123','Toronto', '2019-06-04');
insert into users values ('u014','Stanley', '123','Calgary', '2019-06-05');
insert into users values ('u015','Riley', '123','Toronto', '2019-06-06');
insert into users values ('u016','Haley', '123','Ottawa', '2019-06-08');
insert into users values ('u017','Inactive Man','123','Edmonton','2019-06-09');
insert into users values ('u018','Joe Schmo','123','Mumbai','2019-06-10');

insert into badges values ('astounding question','gold');
insert into badges values ('incredible question', 'gold');
insert into badges values ('fantastic answer','gold');
insert into badges values ('epic answer','gold');
insert into badges values ('ultra user','gold');
insert into badges values ('renowned user','gold');
insert into badges values ('original question','silver');
insert into badges values ('original answer','silver');
insert into badges values ('nice try question','bronze');
insert into badges values ('nice try answer','bronze');
insert into badges values ('commentator user','bronze');
insert into badges values ('unoriginal answer','plastic');
insert into badges values ('unoriginal question','plastic');
insert into badges values ('nothing better to do user','plastic');


insert into ubadges values ('u002', '2019-06-10', 'ultra user');
insert into ubadges values ('u003', '2019-06-11', 'renowned user');

insert into posts values ('p001','2019-01-06','What can I do to earn badges?', 'What kind of posts do people tend to give out badges for?','u001');
insert into questions values ('p001', null);
insert into tags values ('p001','badges');
insert into votes values ('p001',1,'2019-01-06','u001');
insert into posts values ('p002','2019-01-06','Quality, not quantity','Think of innovative original questions that are intriguing or answers that are brief but easy to understand!','u002');
insert into answers values ('p002','p001');
insert into tags values ('p002','original');
insert into posts values ('p003','2019-02-05','Be yourself!','The best thing you can do is provide your own original perspective','u003');
insert into answers values ('p003','p001');
insert into tags values ('p003','unique'); 
insert into posts values ('p008', '2019-03-12','Avoid negativity', 'Whatever you do, do not be negative','u001');
insert into answers values ('p008','p001');
insert into votes values ('p002',1,'2019-01-07','u002');
insert into votes values ('p002',2,'2019-01-07','u001');
insert into votes values ('p002',3,'2019-01-11','u003');
insert into ubadges values ('u001', '2019-05-06', 'astounding question');

insert into posts values ('p004', '2019-02-05','How will governing change in the next decade?','How will governments evolve with the current state of the world?','u004');
insert into questions values ('p004', null);
insert into tags values ('p004', 'government');
insert into tags values ('p004', 'world');
insert into tags values ('p004', 'life');
insert into tags values ('p004', 'society');
insert into posts values ('p005', '2019-02-05','True global cooperation with climate change','I think as climate change gets worse, countries will have no choice but to cooperate together to keep the earth sustainable. In short, there will be drastic changes to the way people consume goods in an effort to prevent our extinction as a species.','u001');
insert into answers values ('p005', 'p004');
insert into tags values ('p005', 'climate change');
insert into tags values ('p005', 'life');
insert into tags values ('p005', 'society');
insert into votes values ('p005',1,'2019-02-06','u001');
insert into votes values ('p005',2,'2019-02-07','u002');
insert into ubadges values ('u004', '2019-02-07', 'incredible question');

insert into posts values ('p006', '2019-03-10', 'Relational algebra', 'What makes the relational algebra queries unique?','u005');
insert into questions values ('p006', null);
insert into tags values ('p006', 'Relational');
insert into tags values ('p006', 'Algebra');
insert into tags values ('p006', 'Database');
insert into tags values ('p006', 'queries');
insert into tags values ('p006', 'unique');

insert into posts values ('p007', '2019-03-11', 'ReLaTiOnAl DaTaBaSe SQL Queries', 'What are some example of sql queries?','u005');
insert into questions values ('p007', null);
insert into tags values ('p007', 'relational');
insert into tags values ('p007', 'database');
insert into tags values ('p007', 'queries');
insert into tags values ('p007', 'sql');

insert into posts values ('p009', '2019-03-14', 'How do you succeed in life?', 'What are some tried-and-true methods to succeed in every aspect of life?', 'u001');
insert into questions values ('p009', null);
insert into tags values ('p009', 'success');
insert into tags values ('p009', 'life');
insert into posts values ('p010', '2019-03-14', 'Keep failing', 'Most success stories do not happen without a lot of failure. People who succeed have a drive that keeps them going despite those failures.', 'u001');
insert into answers values ('p010', 'p009');
insert into votes values ('p010',1,'2019-03-15','u001');

insert into posts values ('p011', '2019-05-14', 'How do you rob your childs piggy bank?', 'What is the best way to rob your child without them noticing? I am at a desperate point in life', 'u001');
insert into questions values ('p011', null);
insert into tags values ('p011', 'life');
insert into tags values ('p011', 'child');
insert into tags values ('p011', 'piggy bank');
insert into posts values ('p012', '2019-05-14', 'Screwdriver', 'If you really have to, use a screwdriver, do not shatter the piggy bank or else they will definitely notice.', 'u001');
insert into answers values ('p012', 'p011');
insert into tags values ('p012', 'life');
insert into tags values ('p012', 'money');
insert into tags values ('p012', 'piggy bank');
insert into tags values ('p012', 'screwdriver');
insert into votes values ('p012',1,'2019-05-15','u001');
insert into votes values ('p012',2,'2019-05-15','u002');
insert into votes values ('p012',3,'2019-05-16','u003');
insert into votes values ('p012',4,'2019-05-17','u004');
insert into ubadges values ('u001', '2019-05-17', 'incredible question');

insert into posts values ('p013', '2019-05-14', 'What are the ethical ramifications of artificial intelligence?', 'As AI gets more and more advanced, will they need their own class of ethics? In other words, do they need to be treated differently than humans?','u004');
insert into questions values ('p013', null);
insert into tags values ('p013', 'ethics');
insert into tags values ('p013', 'life');
insert into tags values ('p013', 'AI');
insert into tags values ('p013', 'society');
insert into votes values ('p013',1,'2019-05-14','u004');
insert into votes values ('p013',2,'2019-05-15','u002');
insert into votes values ('p013',3,'2019-05-15','u001');
insert into votes values ('p013',4,'2019-05-16','u003');
insert into votes values ('p013',5,'2019-05-16','u005');
insert into posts values ('p014','2019-05-14','','Ethic systems tend to evolve with the drive of the human race to survive. AI is fascinating in the sense that humans can instill their own sense of ethics in AI to follow common sense rules.','u001');
insert into answers values ('p014', 'p013');
insert into tags values ('p014', 'society');
insert into tags values ('p014', 'ethics');
insert into tags values ('p014', 'law');
insert into posts values ('p015','2019-05-14','','People should have moral obligations to their machines, just like we have moral obligations to animals. I think we will live to see robot rights being a real thing.','u004');
insert into answers values ('p015', 'p013');
insert into tags values ('p015', 'robot');
insert into tags values ('p015', 'rights');
insert into tags values ('p015', 'society');
insert into ubadges values ('u004', '2019-05-14', 'incredible question');
insert into ubadges values ('u004', '2019-05-15', 'epic answer');

insert into posts values ('p016', '2019-05-14', 'What do we benefit from exploring space?','What is the point of exploring space? I don''t see how it''s beneficial whatsoever.','u005');
insert into questions values ('p016', null);
insert into tags values ('p016', 'space');
insert into posts values ('p017', '2019-05-14', 'There are so many reasons','There are so many societal benefits for everyone on earth that stems from space exploration. We innovate with new tech and knowledge, enrich our culture and inspire many to understand humanity''s place in the universe.','u002');
insert into answers values ('p017', 'p016');
insert into tags values ('p017', 'space');
insert into tags values ('p017', 'society');
insert into tags values ('p017', 'universe');
insert into tags values ('p017', 'benefits');
insert into votes values ('p017',1,'2019-05-14','u010');
insert into votes values ('p017',2,'2019-05-15','u009');
insert into votes values ('p017',3,'2019-05-15','u008');
insert into votes values ('p017',4,'2019-05-16','u007');
insert into votes values ('p017',5,'2019-05-16','u006');
insert into posts values ('p118', '2019-05-14', 'The costs outweigh the benefits', 'When there are so many problems that need to be addressed here and now on earth, we are needlessly focusing so much talent, money and effort towards silly dreams. All of that energy could be diverted to solve the societal problems affecting humanity today. We should not be exploring space until we squash things like climate change, poverty and disease.','u007');
insert into answers values ('p118', 'p016');
insert into tags values ('p118', 'space');
insert into tags values ('p118', 'society');
insert into tags values ('p118', 'climate change');
insert into votes values ('p118',1,'2019-05-14','u005');
insert into votes values ('p118',2,'2019-05-15','u003');
insert into votes values ('p118',3,'2019-05-16','u004');
insert into votes values ('p118',4,'2019-05-18','u002');
insert into votes values ('p118',5,'2019-05-17','u001');
insert into votes values ('p118',6,'2019-05-19','u006');
insert into ubadges values ('u005', '2019-05-14', 'astounding question');
insert into ubadges values ('u002', '2019-05-14', 'fantastic answer');

insert into posts values ('p018','2020-09-20','How do you take care of plants?','What are the common rule of thumbs to gardening?','u016');
insert into questions values ('p018', null);
insert into tags values ('p018', 'plants');
insert into tags values ('p018', 'gardening');
insert into posts values ('p019','2020-09-21','7 rule of thumbs','1. understand each plant has its own needs 2. soil is important 3. keep a watering calendar 4. stick your thumb into soil to see if the plant is dry 5. pull out diseased plants 6. dig the right hole 7. take your time and have fun!','u001');
insert into answers values ('p019', 'p018');
insert into tags values ('p019', 'rules');
insert into tags values ('p019', 'gardening');
insert into tags values ('p019', 'fun');
insert into votes values ('p019',1,'2020-09-21','u016');
insert into votes values ('p019',2,'2020-09-21','u009');
insert into votes values ('p019',3,'2020-09-22','u010');
insert into votes values ('p019',4,'2020-09-22','u015');
insert into votes values ('p019',5,'2020-09-23','u001');
insert into votes values ('p019',6,'2020-09-23','u002');
insert into votes values ('p019',7,'2020-09-24','u004');
insert into votes values ('p019',8,'2020-09-24','u005');
insert into votes values ('p019',9,'2020-09-25','u006');
insert into ubadges values ('u016', '2020-09-20', 'astounding question');
insert into ubadges values ('u001', '2020-09-20', 'fantastic answer');
insert into ubadges values ('u001', '2020-09-21', 'ultra user');
update questions set theaid = 'p019' where pid = 'p018';

insert into posts values ('p020', '2020-09-21', 'What will be the next big thing?','What will be the next best invention that influences our lives to the extent of smart phones?','u001');
insert into questions values ('p020', null);
insert into tags values ('p020', 'innovation');
insert into tags values ('p020', 'invention');
insert into votes values ('p020',1,'2020-09-21','u001');
insert into posts values ('p021', '2020-09-21', 'Augmented Reality', 'Augmented reality will allow us to do so much more, with just-in-time information accessible anytime, anywhere', 'u001');
insert into answers values ('p021', 'p020');
insert into tags values ('p021', 'augmented');
insert into tags values ('p021', 'reality');
insert into tags values ('p021', 'information');
insert into tags values ('p021', 'access');
insert into votes values ('p021',1,'2020-09-21','u001');
insert into posts values ('p022', '2020-09-21', 'nanorobotics','Nanorobotics could become advanced enough to identify and destroy cancer cells, or deliver drugs. This may just be the thing that eradicates cancer.','u016');
insert into answers values ('p022', 'p020');
insert into tags values ('p022', 'nano');
insert into tags values ('p022', 'robotics');
insert into tags values ('p022', 'cancer');
insert into tags values ('p022', 'diseases');
insert into votes values ('p022',1,'2020-09-21','u016');
insert into votes values ('p022',2,'2020-09-21','u002');
insert into votes values ('p022',3,'2020-09-21','u009');
insert into votes values ('p022',4,'2020-09-22','u010');
insert into votes values ('p022',5,'2020-09-22','u007');
insert into votes values ('p022',6,'2020-09-22','u006');
insert into votes values ('p022',7,'2020-09-23','u005');
insert into votes values ('p022',8,'2020-09-23','u004');
insert into votes values ('p022',9,'2020-09-24','u003');
insert into votes values ('p022',10,'2020-09-23','u001');
insert into votes values ('p022',11,'2020-09-23','u008');
insert into votes values ('p022',12,'2020-09-24','u011');
insert into posts values ('p023', '2020-09-22', 'zero carbon natural gas','The ability to efficiently and cheaply capture carbon released by natural gas may very well be the most important way to reverse climate change','u002');
insert into answers values ('p023', 'p020');
insert into tags values ('p023', 'climate change');
insert into tags values ('p023', 'carbon');
insert into tags values ('p023', 'natural gas');
insert into tags values ('p023', 'sustainability');
insert into posts values ('p024', '2020-09-22', 'Autonomous vehicles','We already have the technology to achieve autonomous vehicle and it only needs a final push to be everywhere. This will be like changing from horse carriages to cars all over again.','u004');
insert into answers values ('p024', 'p020');
insert into tags values ('p024', 'autonomous');
insert into tags values ('p024', 'vehicles');
insert into tags values ('p024', 'AI');
insert into votes values ('p024',1,'2020-09-22','u004');
insert into votes values ('p024',2,'2020-09-22','u002');
insert into votes values ('p024',3,'2020-09-23','u001');
insert into votes values ('p024',4,'2020-09-23','u010');
insert into votes values ('p024',5,'2020-09-24','u007');
insert into ubadges values ('u001', '2020-09-22', 'incredible question');
insert into ubadges values ('u016', '2020-09-21', 'fantastic answer');
insert into ubadges values ('u016', '2020-09-22', 'renowned user');
insert into ubadges values ('u004', '2020-09-22', 'epic answer');
update questions set theaid = 'p022' where pid = 'p020';

insert into posts values ('p025','2020-09-23','Do you enjoy working from home?','Does anyone enjoy the ability to work from home?','u002');
insert into tags values ('p025', 'work');
insert into tags values ('p025', 'home');
insert into questions values ('p025',null);

insert into posts values ('p026', '2020-09-24', 'Cake or Pie?','What''s better? Cake or Pie?','u001');
insert into questions values ('p026',null);
insert into tags values ('p026', 'cake');
insert into tags values ('p026', 'pie');
insert into votes values ('p026',1,'2020-09-24','u001');
insert into votes values ('p026',2,'2020-09-24','u004');
insert into votes values ('p026',3,'2020-09-25','u002');
insert into votes values ('p026',4,'2020-09-25','u008');
insert into votes values ('p026',5,'2020-09-26','u016');
insert into votes values ('p026',6,'2020-09-26','u006');
insert into posts values ('p027', '2020-09-24', 'Cake', 'Cake, no contest.', 'u001');
insert into answers values ('p027', 'p026');
insert into tags values ('p027', 'cake');
insert into votes values ('p027',1,'2020-09-24','u001');
insert into posts values ('p028', '2020-09-24', 'Pie','Pie, no contest.','u002');
insert into answers values ('p028', 'p026');
insert into tags values ('p028', 'pie');
insert into votes values ('p028',1,'2020-09-24','u002');
insert into votes values ('p028',2,'2020-09-24','u003');
insert into votes values ('p028',3,'2020-09-25','u005');
insert into posts values ('p029', '2020-09-25', 'Piecake','Why not both?','u016');
insert into answers values ('p029', 'p026');
insert into tags values ('p029', 'pie');
insert into tags values ('p029', 'cake');
insert into ubadges values ('u016', '2020-09-25', 'fantastic answer');
update questions set theaid = 'p028' where pid = 'p026';

insert into posts values ('p030', '2020-09-26', 'What are the best websites that no one knows about?','Do you know any?','u002');
insert into questions values ('p030',null);
insert into tags values ('p030', 'websites');
insert into tags values ('p030', 'unknown');
insert into tags values ('p030', 'best');
insert into votes values ('p030',1,'2020-09-26','u001');
insert into votes values ('p030',2,'2020-09-26','u003');
insert into votes values ('p030',3,'2020-09-26','u002');
insert into votes values ('p030',4,'2020-09-26','u005');
insert into votes values ('p030',5,'2020-09-26','u016');
insert into posts values ('p031', '2020-09-27', 'https://oldgamesdownload.com/', 'Has most pc games between 1970-2000 and is absolutely free', 'u016');
insert into answers values ('p031', 'p030');
insert into tags values ('p031', 'games');
insert into tags values ('p031', 'free');
insert into votes values ('p031',1,'2020-09-26','u001');
insert into votes values ('p031',2,'2020-09-26','u002');
insert into votes values ('p031',3,'2020-09-26','u003');
insert into votes values ('p031',4,'2020-09-26','u004');
insert into votes values ('p031',5,'2020-09-26','u005');
insert into votes values ('p031',6,'2020-09-27','u006');
insert into votes values ('p031',7,'2020-09-27','u007');
insert into votes values ('p031',8,'2020-09-27','u008');
insert into votes values ('p031',9,'2020-09-28','u009');
insert into votes values ('p031',10,'2020-09-28','u010');
insert into votes values ('p031',11,'2020-09-28','u016');
insert into posts values ('p032', '2020-09-27', 'https://tastedive.com/', 'Recommends you similar media to the ones you love', 'u003');
insert into answers values ('p032', 'p030');
insert into tags values ('p032', 'media');
insert into tags values ('p032', 'similar');
insert into votes values ('p032',1,'2020-09-27','u001');
insert into votes values ('p032',2,'2020-09-27','u002');
insert into votes values ('p032',3,'2020-09-28','u003');
insert into votes values ('p032',4,'2020-09-28','u004');
insert into votes values ('p032',5,'2020-09-29','u005');
insert into posts values ('p033', '2020-09-27', 'https://regex101.com/', 'An amazing learning and explenation tool for regex', 'u005');
insert into answers values ('p033', 'p030');
insert into tags values ('p033', 'regex');
insert into tags values ('p033', 'learning');
insert into votes values ('p033',1,'2020-09-27','u006');
insert into votes values ('p033',2,'2020-09-28','u007');
insert into votes values ('p033',3,'2020-09-28','u008');
insert into posts values ('p034', '2020-09-27', 'https://sandspiel.club/', 'A fun sandbox game to waste time on', 'u004');
insert into answers values ('p034', 'p030');
insert into tags values ('p034', 'sandbox');
insert into tags values ('p034', 'games');
insert into votes values ('p034',1,'2020-09-27','u009');
insert into votes values ('p034',2,'2020-09-28','u010');
insert into votes values ('p034',3,'2020-09-28','u011');
insert into ubadges values ('u002', '2020-09-26', 'astounding question');
insert into ubadges values ('u016', '2020-09-26', 'fantastic answer');
insert into ubadges values ('u016', '2020-09-27', 'original answer');
insert into ubadges values ('u003', '2020-09-27', 'epic answer');
insert into ubadges values ('u005', '2020-09-28', 'fantastic answer');
insert into ubadges values ('u004', '2020-09-27', 'fantastic answer');
insert into ubadges values ('u004', '2020-09-28', 'nice try answer');
update questions set theaid = 'p031' where pid = 'p030';

insert into posts values ('p035', '2020-09-27', 'Which job is a lot less fun than expected?','Do you know any careers that are absolutely ungratifying?','u016');
insert into questions values ('p035',null);
insert into tags values ('p035', 'job');
insert into tags values ('p035', 'career');
insert into tags values ('p035', 'ungratifying');
insert into votes values ('p035',1,'2020-09-27','u016');
insert into votes values ('p035',2,'2020-09-27','u015');
insert into votes values ('p035',3,'2020-09-27','u014');
insert into votes values ('p035',4,'2020-09-28','u012');
insert into votes values ('p035',5,'2020-09-28','u009');
insert into posts values ('p036', '2020-09-27', 'Archeologist', 'The pay is bad and you hardly ever find anything worthwhile','u001');
insert into answers values ('p036','p035');
insert into tags values ('p036', 'archeology');
insert into votes values ('p036',1,'2020-09-27','u001');
insert into votes values ('p036',2,'2020-09-28','u002');
insert into votes values ('p036',3,'2020-09-28','u004');
insert into posts values ('p037', '2020-09-27', 'Zookeeper', 'The stenches involved in this job will never stop making you gag','u002');
insert into answers values ('p037','p035');
insert into tags values ('p037', 'zooology');
insert into tags values ('p037', 'smell');
insert into votes values ('p037',1,'2020-09-27','u009');
insert into votes values ('p037',2,'2020-09-28','u010');
insert into posts values ('p038', '2020-09-27', 'Chef', 'The stress involved is enough to give anyone a breakdown','u005');
insert into answers values ('p038','p035');
insert into tags values ('p038', 'cooking');
insert into tags values ('p038', 'chef');
insert into tags values ('p038', 'stress');
insert into votes values ('p038',1,'2020-09-27','u005');
insert into ubadges values ('u016', '2020-09-28', 'astounding question');
insert into ubadges values ('u016', '2020-09-29', 'incredible question');
insert into ubadges values ('u001', '2020-09-27', 'original answer');
insert into ubadges values ('u001', '2020-09-28', 'epic answer');
insert into ubadges values ('u002', '2020-09-27', 'fantastic answer');
insert into ubadges values ('u002', '2020-09-28', 'original answer');
insert into ubadges values ('u005', '2020-09-27', 'original answer');
insert into ubadges values ('u005', '2020-09-29', 'nice try answer');
update questions set theaid = 'p036' where pid = 'p035';

insert into posts values ('p039', '2020-09-28', 'How do you like your eggs?', 'What is the best way to cook an egg?','u001');
insert into questions values ('p039',null);
insert into tags values ('p039', 'eggs');
insert into tags values ('p039', 'cooking');
insert into posts values ('p040', '2020-09-28', 'Scrambled', 'You cannot beat a nice scrambled egg', 'u001');
insert into answers values ('p040','p039');
insert into tags values ('p040', 'eggs');
insert into tags values ('p040', 'scrambled');
insert into votes values ('p040',1,'2020-09-28','u001');
insert into votes values ('p040',2,'2020-09-28','u016');
insert into votes values ('p040',3,'2020-09-28','u009');
insert into votes values ('p040',4,'2020-09-28','u007');
insert into votes values ('p040',5,'2020-09-28','u008');
insert into votes values ('p040',6,'2020-09-28','u003');
insert into votes values ('p040',7,'2020-09-28','u004');
insert into votes values ('p040',8,'2020-09-28','u015');
insert into posts values ('p041', '2020-09-28', 'Hard Boiled', '', 'u002');
insert into answers values ('p041','p039');
insert into tags values ('p041', 'eggs');
insert into tags values ('p041', 'hard boiled');
insert into votes values ('p041',1,'2020-09-28','u002');
insert into posts values ('p042', '2020-09-28', 'Sunny Side Up', '', 'u003');
insert into answers values ('p042','p039');
insert into tags values ('p042', 'eggs');
insert into tags values ('p042', 'sunny side up');
insert into votes values ('p042',1,'2020-09-28','u002');
insert into votes values ('p042',2,'2020-09-28','u001');
insert into votes values ('p042',3,'2020-09-28','u016');
insert into votes values ('p042',4,'2020-09-28','u015');
insert into posts values ('p043', '2020-09-28', 'Over Easy', '', 'u004');
insert into answers values ('p043','p039');
insert into tags values ('p043', 'eggs');
insert into tags values ('p043', 'over easy');
insert into posts values ('p044', '2020-09-28', 'Over Medium', '', 'u005');
insert into answers values ('p044','p039');
insert into tags values ('p044', 'eggs');
insert into tags values ('p044', 'over medium');
insert into votes values ('p044',1,'2020-09-28','u005');
insert into votes values ('p044',2,'2020-09-28','u006');
insert into votes values ('p044',3,'2020-09-28','u007');
insert into posts values ('p045', '2020-09-28', 'Poached!', '', 'u006');
insert into answers values ('p045','p039');
insert into tags values ('p045', 'eggs');
insert into tags values ('p045', 'poached');
insert into votes values ('p045',1,'2020-09-28','u006');
insert into votes values ('p045',2,'2020-09-28','u009');
insert into votes values ('p045',3,'2020-09-28','u010');
insert into ubadges values ('u003', '2020-09-28', 'original answer');
update questions set theaid = 'p040' where pid = 'p039';

insert into posts values ('p046','2020-09-28','What do you think about relational databases?','','u002');
insert into tags values ('p046', 'relational');
insert into tags values ('p046', 'database');
insert into questions values ('p046',null);
insert into posts values ('p049','2020-10-02','They''re super duper awesome','','u006');
insert into answers values ('p049','p046');

insert into posts values ('p047', '2020-10-01','Relationals?','?','u003');
insert into tags values ('p047', 'relational');
insert into questions values ('p047',null);
insert into posts values ('p048', '2020-10-01','Are you talking about relational databases?','what are you talking about?','u005');
insert into tags values ('p048', 'relational');
insert into tags values ('p048', 'database');
insert into answers values ('p048','p047');

insert into posts values ('p050', '2020-10-02', 'What do you love about life the most?','','u008');
insert into tags values ('p050', 'life');
insert into questions values ('p050', null);
insert into posts values ('p051', '2020-10-05', 'The happy moments','','u009');
insert into answers values ('p051','p050');
insert into tags values ('p051', 'life');
insert into tags values ('p051', 'happy');
insert into tags values ('p051', 'moments');

insert into posts values ('p052', '2020-10-03', 'Where do you see yourself in 10 years?','','u004');
insert into tags values ('p052', 'ten years');
insert into questions values ('p052', null);